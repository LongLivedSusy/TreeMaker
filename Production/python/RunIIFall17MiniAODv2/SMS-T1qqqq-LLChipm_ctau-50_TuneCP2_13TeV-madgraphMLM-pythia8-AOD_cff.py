import FWCore.ParameterSet.Config as cms

maxEvens = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFils = cms.untracked.vstring()
secFile = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
] )
