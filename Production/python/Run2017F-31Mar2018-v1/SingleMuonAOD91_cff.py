import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/50016/AAE9DF0E-37E4-E711-BC33-1866DA85DC53.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70002/DA02B88C-95E1-E711-9F3A-001517FB141C.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70002/40DDFC4C-A0E1-E711-BB26-001E67D195F0.root',
] )
