#!/bin/env python
import os, glob
from GridEngineTools import runParallel
import commands

campaigns = { 
              #"PrivateSamples": {
              #                    "scenario": "Fall17Fastsig",
              #                    "cmsswpath": "/nfs/dust/cms/user/kutznerv/shorttrack/treemaker/CMSSW_9_4_11/src",
              #                    "inputFilesConfigs": [
              #                                       "sam_RunIIFall17-T2bt-LLChipm-AOD",
              #                                       "sam_RunIIFall17-T1btbt-LLChipm-AOD",
              #                                       "sam_RunIIFall17-T2tb-LLChipm-AOD",
              #                                       ]
              #                   },
              "RunIIFall17FS": {
                                  "scenario": "Fall17Fastsig",
                                  "cmsswpath": "/nfs/dust/cms/user/kutznerv/shorttrack/treemaker/CMSSW_9_4_11/src",
                                  "inputFilesConfigs": [
                                                     "PMSSM_set_semiLL-AOD",
                                                     "PMSSM_set_semiLL_part10-AOD",
                                                     "PMSSM_set_semiLL_part1-AOD",
                                                     "PMSSM_set_semiLL_part2-AOD",
                                                     "PMSSM_set_semiLL_part3-AOD",
                                                     "PMSSM_set_semiLL_part4-AOD",
                                                     "PMSSM_set_semiLL_part5-AOD",
                                                     "PMSSM_set_semiLL_part6-AOD",
                                                     "PMSSM_set_semiLL_part7-AOD",
                                                     "PMSSM_set_semiLL_part8-AOD",
                                                     "PMSSM_set_semiLL_part9-AOD",
                                                     ]
                                 },
              }

cmds = []
output_folder = "srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub/ProductionRun2v3/"
redo_miniaod = False

for campaign in campaigns:

    print campaign

    for inputFilesConfig in campaigns[campaign]["inputFilesConfigs"]:
        print inputFilesConfig

        if "PMSSM" in inputFilesConfig:
            print "Will re-create miniAODs..."
            redo_miniaod = True
        
        status, file_names = commands.getstatusoutput("grep .root ../python/%s/%s_cff.py | grep '#' -v " % (campaign, inputFilesConfig))
        file_names = file_names.split("\n")
        this_inputFilesConfig = "%s.%s" % (campaign, inputFilesConfig)
        
        for i, file_name in enumerate(file_names):

            if "'" not in file_name: continue

            file_name = file_name.split("'")[1]
            miniaod_infile = file_name
            file_name = "-".join(file_name.split("/")[-5:])
            file_name = file_name.replace(".root", "")
            #file_name = file_name.replace("RunIIFall17__", "RunIIFall17FSv2.")
            file_name = file_name.replace("RunIIFall17.",  "RunIIFall17FSv3.")
            file_name = file_name.replace("RunIIFall17__", "RunIIFall17FSv3.")

            #cmsrun = """singularity exec --contain --bind /afs:/afs --bind /nfs:/nfs --bind /pnfs:/pnfs --bind /cvmfs:/cvmfs --bind /var/lib/condor:/var/lib/condor --bind /tmp:/tmp --pwd . ~/dust/slc6_latest.sif sh -c 'source /cvmfs/cms.cern.ch/cmsset_default.sh; cd /afs/desy.de/user/k/kutznerv/dust/shorttrack/treemaker/CMSSW_9_4_11/src/TreeMaker/Production/test/;
            #          eval `scramv1 runtime -sh`; $MINIAODCMD
            #          cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=%s inputFilesConfig=%s nstart=%s nfiles=1 outfile=%s;
            #          source /cvmfs/grid.desy.de/etc/profile.d/grid-ui-env.sh;
            #          cd /afs/desy.de/user/k/kutznerv/dust/shorttrack/treemaker/CMSSW_9_4_11/src/TreeMaker/Production/test/;
            #          rootls %s_RA2AnalysisTree.root:TreeMaker2 | grep PreSelection && (eval `scram unsetenv -sh`; gfal-copy -f %s_RA2AnalysisTree.root %s) || echo "Failed!";
            #          rm %s_RA2AnalysisTree.root'""" % (campaigns[campaign]["scenario"], this_inputFilesConfig, i, file_name, file_name, file_name, output_folder, file_name)

            cmsrun = """cd $CMSSW_BASE/src/TreeMaker/Production/test/; eval `scramv1 runtime -sh`; $MINIAODCMD
                      cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=%s inputFilesConfig=%s nstart=%s nfiles=1 outfile=%s numevents=-1;
                      source /cvmfs/grid.cern.ch/umd-sl6ui-latest/etc/profile.d/setup-ui-example.sh;
                      rootls %s_RA2AnalysisTree.root:TreeMaker2 | grep PreSelection && (eval `scram unsetenv -sh`; srmcp file://$(pwd)/%s_RA2AnalysisTree.root %s) || echo "Failed!";
                      rm %s_RA2AnalysisTree.root""" % (campaigns[campaign]["scenario"], this_inputFilesConfig, i, file_name, file_name, file_name, output_folder + file_name.split("/")[-1] + ".root", file_name)
           
            if redo_miniaod:
                cmsrun = cmsrun.replace("$MINIAODCMD", "pwd; echo 'miniaod.root' > info_miniaods; cat info_miniaods; ../aod_support/convert_AOD_to_miniAOD.py --infile=%s --outfile=miniaod.root --nev=-1; ls -l; " % (miniaod_infile) )
            else:
                cmsrun = cmsrun.replace("$MINIAODCMD", "")
            
            # check if outputfile already exists...
            outfile = "%s/%s_RA2AnalysisTree.root" % (output_folder.replace("srm://dcache-se-cms.desy.de", ""), file_name)
            if os.path.exists(outfile):
                if os.path.getsize(outfile)<20000:
                    cmds.append(cmsrun.replace("\n", ""))
            else:
                cmds.append(cmsrun.replace("\n", ""))

print "There are %s files to process" % len(cmds)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
cmds = list(chunks(cmds, 3))
for i in range(len(cmds)):
    cmds[i] = "; ".join(cmds[i])

cmds = cmds[:4000]
#cmds = cmds[:1]

print len(cmds)
bigchunks = list(chunks(cmds, 4999))
for i_bigchunk, bigchunk in enumerate(bigchunks):
    #runParallel(bigchunk, "grid", use_sl6=True, condorDir="condor2017FSSam_%s" % i_bigchunk, confirm=False)
    runParallel(bigchunk, "grid", use_sl6=True, condorDir="condorPMSSM_%s" % i_bigchunk, use_more_time=21600, confirm=False, tarball=True, recreateTarball=True, cmsbase="/afs/desy.de/user/k/kutznerv/dust/shorttrack/treemaker/CMSSW_9_4_11")


