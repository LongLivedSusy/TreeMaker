import FWCore.ParameterSet.Config as cms

maxEvents =cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles =cms.untracked.vstring()
secFiles = ms.untracked.vstring()
source = cm.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
] )
