import FWCore.ParameterSet.Config as cms

# import functions to be assigned as class methods
from TreeMaker.TreeMaker.makeTreeFromMiniAOD_cff import makeTreeFromMiniAOD
from TreeMaker.TreeMaker.makeJetVars import makeJetVars, makeMHTVars, makeGoodJets, makeJetVarsAK8
from TreeMaker.TreeMaker.doHadTauBkg import doHadTauBkg, makeJetVarsHadTau
from TreeMaker.TreeMaker.doLostLeptonBkg import doLostLeptonBkg
from TreeMaker.TreeMaker.doZinvBkg import doZinvBkg, reclusterZinv

import os
def getAODfromMiniAODPath(datasetPathMiniAOD):

	print "getAODfromMiniAODPath" , datasetPathMiniAOD
	filepathbits = datasetPathMiniAOD.split('/store')
	if len(filepathbits)==2:
		filepathbits[1] = '/store'+filepathbits[1]
	# get AOD file(s) from MiniAOD file path

	# fix SSL site configuration for DAS client:
	os.environ['SSL_CERT_DIR'] = '/etc/pki/tls/certs:/etc/grid-security/certificates'

	#parentfiles = check_output(["./data/das_client.py", '--query=parent file=%s' % datasetPathMiniAOD, '--limit=0']) .split()
	parentfiles = []
	print 'dasgoclient --query="parent file='+filepathbits[1]+'" --limit=0 > '+'tmp.txt'
	os.system('dasgoclient --query="parent file='+filepathbits[1]+'" --limit=0 > '+'tmp.txt')
	ftmp = open('tmp.txt')
	lines = ftmp.readlines()
	ftmp.close()
	os.system('rm tmp.txt')
	for line in lines: parentfiles.append(line.strip())

	aodFiles = []
	for parentfile in parentfiles:
		if "/AOD" in parentfile:
			# parent file is already AOD file
			aodFiles.append(parentfile)
		else:
			# parent file is e.g. RAW, so check its children:

			# childFiles = check_output(["./data/das_client.py", "--query=child file=%s" % parentfile, '--limit=0']).split()
			childFiles = []
			os.system('dasgoclient --query="child file='+parentfile+'" --limit=0 > '+'tmp.txt')
			ftmp = open('tmp.txt')
			lines = ftmp.readlines()
			ftmp.close()
			os.system('rm tmp.txt')
			for line in lines: childFiles.append(line.strip())

			for childFile in childFiles:
				if "/AOD" in childFile:
					aodFiles.append(childFile)

	# avoid duplicate entries:
	print 'obtained ',len(aodFiles),',file-long aod set:', aodFiles
	return list(set(aodFiles))

class makeTree:
	def __init__(self,parameters):
		self.parameters = parameters

		# auto configuration for different scenarios
		self.scenarioName=self.parameters.value("scenario","")
		from TreeMaker.Production.scenarios import Scenario
		self.scenario = Scenario(self.scenarioName)

		self.getParamDefault("inputFilesConfig","")
		self.getParamDefault("dataset",[])
		self.getParamDefault("sidecar",[])#SB     
		self.getParamDefault("privateSample",False)
		self.getParamDefault("nstart",0)
		self.getParamDefault("nfiles",-1)
		self.getParamDefault("numevents",-1)
		self.getParamDefault("outfile","test_run")
		outfilesuff=self.parameters.value("outfilesuff","_RA2AnalysisTree")
		self.outfile += outfilesuff
		self.getParamDefault("treename","PreSelection")

		# background estimations on by default
		self.getParamDefault("lostlepton", True)
		self.getParamDefault("hadtau", True)
		self.getParamDefault("hadtaurecluster", 0)
		self.getParamDefault("doZinv", True)

		# special signal stuff
		self.getParamDefault("systematics",True);
		self.getParamDefault("semivisible",True);

		# compute the PDF weights
		self.getParamDefault("doPDFs", True);

		# other options off by default
		self.getParamDefault("debugtracks", False)
		self.getParamDefault("applybaseline", False)

		# take command line input (w/ defaults from scenario if specified)
		self.getParamDefault("globaltag",self.scenario.globaltag)
		self.getParamDefault("tagname",self.scenario.tagname)
		self.getParamDefault("geninfo",self.scenario.geninfo)
		self.getParamDefault("pmssm",self.scenario.pmssm)
		self.getParamDefault("fastsim",self.scenario.fastsim)
		self.getParamDefault("signal",self.scenario.signal)
		self.getParamDefault("jsonfile",self.scenario.jsonfile)
		self.getParamDefault("jecfile",self.scenario.jecfile)
		self.getParamDefault("residual",self.scenario.residual)
		self.getParamDefault("jerfile",self.scenario.jerfile)
		self.getParamDefault("pufile",self.scenario.pufile)
		self.getParamDefault("era",self.scenario.era)

		# temporary redirector fix
		# fastsim signal is phedexed to LPC Tier3
		self.getParamDefault("redir", "root://cmseos.fnal.gov/" if self.fastsim and self.signal else "root://cmsxrootd.fnal.gov/")
		# handle site name usage
		if self.redir[0]=="T":
			self.redir = "root://cmsxrootd.fnal.gov//store/test/xrootd/"+self.redir

		# Load input files
		self.readFiles = cms.untracked.vstring()
		self.readFiles_sidecar = cms.untracked.vstring()        #SB

		print 'hello?', '??', self.dataset, self.sidecar, self.nfiles, self.readFiles
		if self.inputFilesConfig!="" :
			readFilesImport = getattr(__import__("TreeMaker.Production."+self.inputFilesConfig+"_cff",fromlist=["readFiles"]),"readFiles")
			if self.nfiles==-1:
				self.readFiles.extend( readFilesImport )
			else:
				self.readFiles.extend( readFilesImport[self.nstart:(self.nstart+self.nfiles)] )
			print 'testing self.readFiles', self.readFiles
		
		if self.dataset!=[] :    
			self.readFiles.extend( [self.dataset] )
	

		for rf in self.readFiles:
			self.readFiles_sidecar += getAODfromMiniAODPath(rf)

		self.readFiles = [(self.redir if val[0:6]=="/store" else "")+val for val in self.readFiles]
		self.readFiles_sidecar = [(self.redir if val[0:6]=="/store" else "")+val for val in self.readFiles_sidecar]
			
		print 'readFiles', self.readFiles
		print 'readFiles_sidecar', self.readFiles_sidecar	
	

		# branches for treemaker
		self.VectorRecoCand             = cms.vstring()
		self.VarsDouble                 = cms.vstring()
		self.VarsInt                    = cms.vstring()
		self.VarsBool                   = cms.vstring()
		self.VectorTLorentzVector       = cms.vstring()
		self.VectorDouble               = cms.vstring()
		self.VectorString               = cms.vstring()
		self.VectorInt                  = cms.vstring()
		self.VectorBool                 = cms.vstring()
		self.VectorVectorTLorentzVector = cms.vstring()

	def getParamDefault(self,param,default):
		setattr(self,param,self.parameters.value(param,default))

	def printSetup(self):
		print " readFiles: "+str(self.readFiles)
		print " with sidecar: "+str(self.readFiles_sidecar)
		print " outfile: "+self.outfile
		print " treename: "+self.treename
		print " "
		print " storing lostlepton variables: "+str(self.lostlepton)
		print " storing hadtau variables: "+str(self.hadtau)+" w/ reclustering "+str(self.hadtaurecluster)
		print " storing Zinv variables: "+str(self.doZinv)
		print " storing semi-visible jet variables: "+str(self.semivisible)
		print " "
		print " storing JEC/JER systematics: "+str(self.systematics)
		print " storing PDF weights: "+str(self.doPDFs)
		print " "
		print " storing track debugging variables: "+str(self.debugtracks)
		print " Applying baseline selection filter: "+str(self.applybaseline)
		print " "
		print " scenario: "+self.scenarioName
		print " global tag: "+self.globaltag
		print " Instance name of tag information: "+self.tagname
		print " Including gen-level information: "+str(self.geninfo)
		print " Including pMSSM-related information: "+str(self.pmssm)
		print " Using fastsim settings: "+str(self.fastsim)
		print " Running signal uncertainties: "+str(self.signal)
		if len(self.jsonfile)>0: print " JSON file applied: "+self.jsonfile
		if len(self.jecfile)>0: print " JECs applied: "+self.jecfile+(" (residuals)" if self.residual else "")
		if len(self.jerfile)>0: print " JERs applied: "+self.jerfile
		if len(self.pufile)>0: print " PU weights stored: "+self.pufile
		print " era of this dataset: "+self.era

	# assign class methods from functions
	makeTreeFromMiniAOD = makeTreeFromMiniAOD
	makeGoodJets = makeGoodJets
	makeJetVars = makeJetVars
	makeJetVarsAK8 = makeJetVarsAK8
	makeMHTVars = makeMHTVars
	doHadTauBkg = doHadTauBkg
	makeJetVarsHadTau = makeJetVarsHadTau
	doLostLeptonBkg = doLostLeptonBkg
	doZinvBkg = doZinvBkg
	reclusterZinv = reclusterZinv
