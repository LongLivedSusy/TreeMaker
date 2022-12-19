import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/MET/AOD/07Aug17_ver2-v1/90000/EEA5526D-FC9D-E711-B0C7-FA163E7DB158.root',
       '/store/data/Run2016B/MET/AOD/07Aug17_ver2-v1/90000/8CAAB491-E8A1-E711-8A65-0CC47A78A446.root',
] )
