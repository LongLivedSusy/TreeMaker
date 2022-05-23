#!/bin/env python
import os, glob
from GridEngineTools import runParallel
import commands

campaigns = { 
              #"Run2018A-17Sep2018-v1": {
              #                            "scenario": "2018ReReco17Sep",
              #                            "cmsswpath": "/nfs/dust/cms/user/kutznerv/shorttrack/treemaker/CMSSW_10_2_7/src",
              #                            "inputFilesConfigs": [
              #                                               "JetHTAOD",
              #                                               "METAOD",
              #                                               "SingleMuonAOD0",
              #                                               "SingleMuonAOD1",
              #                                               "EGammaAOD0",
              #                                               "EGammaAOD1",
              #                                               "EGammaAOD2",
              #                                               "EGammaAOD3",
              #                                               "EGammaAOD4",
              #                                               "EGammaAOD5",
              #                                               "EGammaAOD6",
              #                                               ]
              #                          },
              "Run2018B-17Sep2018-v1": {
                                          "scenario": "2018ReReco17Sep",
                                          "cmsswpath": "/nfs/dust/cms/user/kutznerv/shorttrack/treemaker/CMSSW_10_2_7/src",
                                          "inputFilesConfigs": [
                                                             #"JetHTAOD",
                                                             #"SingleMuonAOD",
                                                             "METAOD",
                                                             #"EGammaAOD0",
                                                             #"EGammaAOD1",
                                                             #"EGammaAOD2",
                                                             ]
                                        },
              #"Run2018C-17Sep2018-v1": {
              #                            "scenario": "2018ReReco17Sep",
              #                            "cmsswpath": "/nfs/dust/cms/user/kutznerv/shorttrack/treemaker/CMSSW_10_2_7/src",
              #                            "inputFilesConfigs": [
              #                                               "JetHTAOD",
              #                                               "METAOD",
              #                                               "SingleMuonAOD",
              #                                               "EGammaAOD0",
              #                                               "EGammaAOD1",
              #                                               "EGammaAOD2",
              #                                               ]
              #                          },
              #"Run2018D-PromptReco-v2": {
              #                            "scenario": "2018PromptReco",
              #                            "cmsswpath": "/nfs/dust/cms/user/kutznerv/shorttrack/treemaker/CMSSW_10_2_7/src",
              #                            "inputFilesConfigs": [
              #                                               #"EGammaAOD0",
              #                                               #"EGammaAOD1",
              #                                               #"EGammaAOD2",
              #                                               #"EGammaAOD3",
              #                                               #"EGammaAOD4",
              #                                               #"EGammaAOD5",
              #                                               #"EGammaAOD6",
              #                                               #"EGammaAOD7",
              #                                               #"EGammaAOD8",
              #                                               #"EGammaAOD9",
              #                                               #"EGammaAOD10",
              #                                               #"EGammaAOD11",
              #                                               #"EGammaAOD12",
              #                                               #"EGammaAOD13",
              #                                               "JetHTAOD",
              #                                               "EGammaAOD",
              #                                               "METAOD",
              #                                               "JetHTAOD0",
              #                                               "JetHTAOD1",
              #                                               "JetHTAOD2",
              #                                               "JetHTAOD3",
              #                                               "JetHTAOD4",
              #                                               "JetHTAOD5",
              #                                               "JetHTAOD6",
              #                                               "METAOD0",
              #                                               "METAOD1",
              #                                               "METAOD2",
              #                                               "SingleMuonAOD0",
              #                                               "SingleMuonAOD1",
              #                                               "SingleMuonAOD2",
              #                                               "SingleMuonAOD3",
              #                                               "SingleMuonAOD4",
              #                                               "SingleMuonAOD5",
              #                                               "SingleMuonAOD6",
              #                                               "SingleMuonAOD7",
              #                                               "SingleMuonAOD8",
              #                                               ]
              #                          },
            }

cmds = []
output_folder = "/nfs/dust/cms/user/kutznerv/NtupleHub/ProductionRun2v3"

for campaign in campaigns:
    print campaign
    for inputFilesConfig in campaigns[campaign]["inputFilesConfigs"]:
        print inputFilesConfig
        
        status, file_names = commands.getstatusoutput("grep .root ../python/%s/%s_cff.py | grep '#' -v " % (campaign, inputFilesConfig))
        file_names = file_names.split("\n")
        this_inputFilesConfig = "%s.%s" % (campaign, inputFilesConfig)
        
        for i, file_name in enumerate(file_names):

            if "'" not in file_name: continue

            file_name = file_name.split("'")[1]
            file_name = this_inputFilesConfig + "_" + file_name.split("/")[-2] + "-" + file_name.split("/")[-1].replace(".root", "")

            #status, check = commands.getstatusoutput("ls /nfs/dust/cms/user/kutznerv/NtupleHub/ProductionRun2v3/*root /afs/desy.de/user/k/kutznerv/dust/shorttrack/treemaker/CMSSW_10_2_7/src/TreeMaker/Production/*/*root | grep %s" % file_name)
            #if status == 0:
            #    print "already done:", file_name
            #    continue

            cmsrun = "cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=%s inputFilesConfig=%s nstart=%s nfiles=1 outfile=%s" % (campaigns[campaign]["scenario"], this_inputFilesConfig, i, file_name)

            cmds.append( """identifier=$RANDOM$RANDOM; cd %s/TreeMaker/Production; eval `scramv1 runtime -sh`; cp -r test test-$identifier; cd test-$identifier; rm info_*; tar -xf catalogues.tar.gz; %s; ./get_miniAOD_filenames_from_catalogue.py --infile=$(cat info_aodfilenames); rm catalogues*; %s; mv *root %s/""" % (campaigns[campaign]["cmsswpath"], cmsrun, cmsrun, output_folder) )

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
cmds = list(chunks(cmds, 10))
for i in range(len(cmds)):
    cmds[i] = "; ".join(cmds[i])
        
runParallel(cmds, "multi", use_sl6=True)

