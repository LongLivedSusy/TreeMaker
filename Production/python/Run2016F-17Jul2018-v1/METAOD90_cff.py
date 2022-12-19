import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016F/MET/AOD/07Aug17-v1/50000/78E81A7E-59A0-E711-8810-4C79BA1811C3.root',
       '/store/data/Run2016F/MET/AOD/07Aug17-v1/50000/4CA8DD30-979F-E711-9B1B-008CFAC93EB4.root',
] )
