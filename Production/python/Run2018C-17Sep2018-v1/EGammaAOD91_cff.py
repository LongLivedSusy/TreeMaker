import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018C/EGamma/AOD/17Sep2018-v1/60000/47109BF9-97FA-6F41-AB4F-766EF5A3BECD.root',
       '/store/data/Run2018C/EGamma/AOD/17Sep2018-v1/110000/17ACFEDC-2DB6-764F-8AB5-90E206A9B188.root',
] )
