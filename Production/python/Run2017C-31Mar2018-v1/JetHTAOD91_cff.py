import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017C/JetHT/AOD/17Nov2017-v1/30002/680AAAD4-90D5-E711-A3C5-FA163E157A31.root',
#       '/store/data/Run2017C/JetHT/AOD/17Nov2017-v1/30003/66683FE6-2BD8-E711-9DE0-001E67E6F431.root',
] )
