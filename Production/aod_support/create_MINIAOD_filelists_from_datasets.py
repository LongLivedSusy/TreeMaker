#!/bin/env python
import os
import glob
import commands

# create AOD file lists from exisiting miniAOD file lists. Configuration:

check_dataset_availablity = True

cff_folder = "../python/RunIISummer16MiniAODv3"
miniaod_datastreams = [
    "/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
    "/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
    "/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
    "/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM",
    "/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM", 
]

for dataset in miniaod_datastreams:

    # get only unique entries in list:
    complete_output = [dataset]
    print "selected MINIAOD dataset:", complete_output
            
    # create python configuration:
    all_filenames = ""
    for item in complete_output:
        status, filenames = commands.getstatusoutput('dasgoclient -query="file dataset=%s"' % item)
        if len(filenames) == 0:
            raw_input("### file list empty, this should not happen: %s" % item)
        all_filenames += "\n" + filenames
    
    # Create a function called "chunks" with two arguments, l and n:
    def dochunks(l, n):
        # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i:i+n]
    
    chunks = list(dochunks(all_filenames.split("\n"), 254))

    os.system("mkdir -p %s" % cff_folder)

    # don't submit more than 78 chunks at once (close to the limit of 20k jobs for CMS Connect):
    chunks_per_submission_file = list(dochunks(chunks, 20))
    for ichunk, filechunks in enumerate(chunks_per_submission_file):

        identifier = dataset.split("/")[1]

        if len(chunks_per_submission_file) == 1:
            pyfilename = cff_folder + "/" + identifier + "-MINIAOD_cff.py"
        else:
            pyfilename = cff_folder + "/" + identifier + "-MINIAOD%s_cff.py" % ichunk

        with open(pyfilename, "w+") as fout:
            header = """import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
"""
       
            fout.write(header)
       
            for chunk in filechunks:
                fout.write("readFiles.extend( [\n")
                for ifile in chunk:
                    if ifile != "":
                        fout.write("'%s',\n" % ifile)
                fout.write("] )\n")
                
        print pyfilename, "written!"
    print "++++++++++++++++++++++++++++++++++++++++++++++++"



