#!/bin/env python
import os
import glob
import commands
from natsort import natsorted, ns

# create cff file containing our signal files:

def dochunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]


def create_filelist(miniAOD_path, pyfilename):
    
    #all_filenames = natsorted(glob.glob(miniAOD_path + "/step3_higgsino_susyall*MINIAODSIM.root"))
    all_filenames = natsorted(glob.glob(miniAOD_path))
    
    chunks = list(dochunks(all_filenames, 254))
    
    with open(pyfilename, "w+") as fout:
        header = """import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
"""
    
        fout.write(header)
    
        for chunk in chunks:
            fout.write("readFiles.extend( [\n")
            for ifile in chunk:
                if ifile != "":
                    fout.write("       'file://%s',\n" % ifile)
            fout.write("] )\n")
            
    print "%s written!" % pyfilename


#create_filelist("/nfs/dust/cms/user/kutznerv/DisappTrksSignalMC/CMSSW10/miniAODSIM/", "../python/PrivateSamples/g1800_chi1400_27_200970_CMSSW10_cff.py")
#create_filelist("/nfs/dust/cms/user/kutznerv/DisappTrksSignalMC/CMSSW8/miniAODSIM/", "../python/PrivateSamples/g1800_chi1400_27_200970_CMSSW8_cff.py")
#create_filelist("/nfs/dust/cms/user/beinsam/LongLiveTheChi/Production/FastScans/step3_test_higgsino_susyall_mChipm105GeV_dm0p36GeV_pu_inMINIAODSIM.root", "../python/PrivateSamples/sam_fasthiggsino.py")
#create_filelist("/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu/", "../python/PrivateSamples/sam_CompressedHiggsino.py")

create_filelist("/pnfs/desy.de/cms/tier2/store/user/sbein/SMS2/RunIIAutumn18.SMS-T1btbt-LLChipm/*/*/*/*.root", "../python/PrivateSamples/sam_RunIIAutumn18-T1btbt-LLChipm-AOD_cff.py")
create_filelist("/pnfs/desy.de/cms/tier2/store/user/sbein/SMS2/RunIIAutumn18.SMS-T2bt-LLChipm/*/*/*/*.root", "../python/PrivateSamples/sam_RunIIAutumn18-T2bt-LLChipm-AOD_cff.py")
create_filelist("/pnfs/desy.de/cms/tier2/store/user/sbein/SMS2/RunIIAutumn18__SMS-T2tb-LLChipm/*/*/*/*.root", "../python/PrivateSamples/sam_RunIIAutumn18-T2tb-LLChipm-AOD_cff.py")

create_filelist("/pnfs/desy.de/cms/tier2/store/user/sbein/SMS2/RunIIFall17__SMS-T1btbt-LLChipm/*/*/*/*.root", "../python/PrivateSamples/sam_RunIIFall17-T1btbt-LLChipm-AOD_cff.py")
create_filelist("/pnfs/desy.de/cms/tier2/store/user/sbein/SMS2/RunIIFall17__SMS-T2bt-LLChipm/*/*/*/*.root", "../python/PrivateSamples/sam_RunIIFall17-T2bt-LLChipm-AOD_cff.py")
create_filelist("/pnfs/desy.de/cms/tier2/store/user/sbein/SMS2/RunIIFall17__SMS-T2tb-LLChipm/*/*/*/*.root", "../python/PrivateSamples/sam_RunIIFall17-T2tb-LLChipm-AOD_cff.py")
