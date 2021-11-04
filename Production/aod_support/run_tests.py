#!/bin/env python
import commands
import os
import glob

# some unit tests for AOD-based ntuple processing:

def runcmd(cmd):
    print "running", cmd
    status, output = commands.getstatusoutput(cmd)
    return status, output


def run_test(sample, scenario):

    print "Testing %s with %s scenario" % (scenario, sample)

    os.chdir("../test/")

    outfile = "test_" + sample.split(".")[-1]
    cmsRun_command = "singularity exec --contain --bind /afs:/afs --bind /nfs:/nfs --bind /pnfs:/pnfs --bind /cvmfs:/cvmfs --bind /var/lib/condor:/var/lib/condor --bind /tmp:/tmp --pwd . ~/dust/slc6_latest.sif sh -c 'source /cvmfs/cms.cern.ch/cmsset_default.sh; cd /nfs/dust/cms/user/kutznerv/shorttrack/treemaker/CMSSW_10_2_7/src/TreeMaker/Production/test/; export SCRAM_ARCH=slc6_amd64_gcc700; eval `scramv1 runtime -sh`; cmsRun runMakeTreeFromMiniAOD_cfg.py outfile=%s inputFilesConfig=%s nstart=100 nfiles=1 scenario=%s numevents=-1'" % (outfile, sample, scenario)

    status, output = runcmd("rm info_*")
    status, output = runcmd(cmsRun_command)
    status, output = runcmd('./get_miniAOD_filenames_from_catalogue.py --infile="$(cat info_aodfilenames)"')
    
    if status == 0:
        status, output = runcmd(cmsRun_command)

    if status == 0:
        print "\n@@@ test successful\n"
    else:
        print output
        print "\n@@@ test failed :-(\n"
    return status


if __name__ == "__main__":

    tests = [
              #["Fall17", "RunIIFall17MiniAODv2.GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8_v2AOD"],
              #["Fall17", "RunIIFall17MiniAODv2.DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8AOD"],
              #["Fall17nowrongPU", "RunIIFall17MiniAODv2.QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8AOD"],
              #["2016MiniAODv3", "Run2016C-17Jul2018-v1.METAOD"],
              #["2016MiniAODv3", "Run2016H-17Jul2018-v2.METAOD"],
              #["2016MiniAODv3", "Run2016H-17Jul2018-v2.METAOD"],
              #["2017ReReco31Mar", "Run2017E-31Mar2018-v1.METAOD"],
              #["2018ReReco17Sep", "Run2018C-17Sep2018-v1.EGammaAOD0"],
              #["2018ReReco17Sep", "Run2018A-17Sep2018-v1.METAOD"],
              #["2018ReReco17Sep", "Run2018B-17Sep2018-v1.METAOD"],
              #["2018PromptReco", "Run2018D-PromptReco-v2.EGammaAOD1"],
              #["Autumn18Fastsig", "RunIIAutumn18FS.PMSSM_set_1_LL_TuneCP2_13TeV-pythia8-AOD0"],
              ["Fall17Fastsig", "RunIIFall17FS.SMS-T1btbt-LLC1_ctau10to200-mGluino-1000to2800-mLSP0to2800_TuneCP2_13TeV-madgraphMLM-pythia8-AOD"],
              #["Fall17Fastsig", "RunIIFall17FS.SMS-T2tb-LLChipm_ctau10to200-mStop-400to1750-mLSP0to1650_TuneCP2_13TeV-madgraphMLM-pythia8-AOD"],
              #["Autumn18Fastsig", "RunIIAutumn18FS.SMS-T1btbt-LLC1_ctau10to200-mGluino-1000to2800-mLSP0to2800_TuneCP2_13TeV-madgraphMLM-pythia8-AOD"],
              #["Summer16MiniAODv3", "RunIISummer16MiniAODv3.DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-AOD"],
              #["Summer16MiniAODv3sig", "RunIISummer16MiniAODv3.SMS-T1qqqq-LLChipm_ctau-200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-AOD"],
              #["Summer16MiniAODv3sig", "RunIISummer16MiniAODv3.SMS-T1qqqq-LLChipm_ctau-200_mLSP-800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8-AOD"],
            ]

    for test in tests:
        run_test(test[1], test[0])

