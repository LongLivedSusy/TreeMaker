import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017E/JetHT/AOD/17Nov2017-v1/40000/147D76CF-65CF-E711-8E95-0025904CF766.root',
       '/store/data/Run2017E/JetHT/AOD/17Nov2017-v1/30002/E60F94E2-C4D5-E711-B745-001E67E6F891.root',
       '/store/data/Run2017E/JetHT/AOD/17Nov2017-v1/30002/542D20A8-C9D5-E711-9BAB-A4BF01125D8E.root',
       '/store/data/Run2017E/JetHT/AOD/17Nov2017-v1/40000/C4BFDF27-89CF-E711-81D4-001E67E71CC2.root',
       '/store/data/Run2017E/JetHT/AOD/17Nov2017-v1/40000/DA6C7883-77CF-E711-A0B9-02163E0176CC.root',
] )
