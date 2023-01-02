import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2016F/SingleMuon/AOD/07Aug17-v1/50000/9092FE07-F18D-E711-A5B5-008CFA197928.root',
#       '/store/data/Run2016F/SingleMuon/AOD/07Aug17-v1/50000/AECD87B3-6D8D-E711-9E60-00259054C796.root',
       '/store/data/Run2016F/SingleMuon/AOD/07Aug17-v1/50001/0A47CB6C-AE8E-E711-B734-008CFA11137C.root',
] )
