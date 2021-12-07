#!/bin/env python
import os, glob
from GridEngineTools import runParallel
import commands

campaigns = { 
              "PrivateSamples": {
                                  "scenario": "Fall17Fastsig",
                                  "cmsswpath": "/nfs/dust/cms/user/kutznerv/shorttrack/treemaker/CMSSW_9_4_11/src",
                                  "inputFilesConfigs": [
                                                     "sam_RunIIFall17-T2bt-LLChipm-AOD",
                                                     "sam_RunIIFall17-T1btbt-LLChipm-AOD",
                                                     "sam_RunIIFall17-T2tb-LLChipm-AOD",
                                                     ]
                                 },
              }

cmds = []
output_folder = "srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/ProductionRun2v3/"

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
            file_name = "-".join(file_name.split("/")[-5:])
            file_name = file_name.replace(".root", "")
            file_name = file_name.replace("RunIIFall17__", "RunIIFall17FSv2.")

            cmsrun = """singularity exec --contain --bind /afs:/afs --bind /nfs:/nfs --bind /pnfs:/pnfs --bind /cvmfs:/cvmfs --bind /var/lib/condor:/var/lib/condor --bind /tmp:/tmp --pwd . ~/dust/slc6_latest.sif sh -c 'source /cvmfs/cms.cern.ch/cmsset_default.sh; cd /afs/desy.de/user/k/kutznerv/dust/shorttrack/treemaker/CMSSW_9_4_11/src/TreeMaker/Production/test/;
                      eval `scramv1 runtime -sh`;
                      cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=%s inputFilesConfig=%s nstart=%s nfiles=1 outfile=%s' ;
                      eval `scram unsetenv -sh`;
                      source /cvmfs/grid.desy.de/etc/profile.d/grid-ui-env.sh;
                      cd /afs/desy.de/user/k/kutznerv/dust/shorttrack/treemaker/CMSSW_9_4_11/src/TreeMaker/Production/test/;
                      gfal-copy -f %s_RA2AnalysisTree.root %s;
                      rm %s_RA2AnalysisTree.root""" % (campaigns[campaign]["scenario"], this_inputFilesConfig, i, file_name, file_name, output_folder, file_name)
            
            # check if outputfile already exists...
            if not os.path.exists("%s/%s_RA2AnalysisTree.root" % (output_folder.replace("srm://dcache-se-cms.desy.de", ""), file_name)):
                cmds.append(cmsrun.replace("\n", ""))

print "There are %s files to process" % len(cmds)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
cmds = list(chunks(cmds, 25))
for i in range(len(cmds)):
    cmds[i] = "; ".join(cmds[i])
        
runParallel(cmds, "grid", use_sl6=False, condorDir="condor2017FSSam", confirm=False)

