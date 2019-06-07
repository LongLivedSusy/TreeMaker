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

#miniAOD_path = "/nfs/dust/cms/user/kutznerv/DisappTrksSignalMC/CMSSW10/miniAODSIM/"
#pyfilename = "../python/PrivateSamples/g1800_chi1400_27_200970_CMSSW10_cff.py"

miniAOD_path = "/nfs/dust/cms/user/kutznerv/DisappTrksSignalMC/CMSSW8/miniAODSIM/"
pyfilename = "../python/PrivateSamples/g1800_chi1400_27_200970_CMSSW8_cff.py"

all_filenames = natsorted(glob.glob(miniAOD_path + "/*root"))
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


