import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/10000/7231E089-D4F7-E711-8C3B-7CD30ACDCE6C.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/40000/5EEE97F9-C206-E811-82FE-0025905B85E8.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/20000/DC2DA888-5805-E811-B181-7CD30ACE1239.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/80000/2048F47D-86FB-E711-B622-0242AC1C0501.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/10002/52677964-C0FA-E711-94E0-00266CFFCD14.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/80000/8E24B68F-14FA-E711-B8E2-A4BF0108B2F2.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/80000/9039F78E-17FA-E711-B52C-001E67792430.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/20002/C8714DAC-6702-E811-BDE4-0025B3E01806.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/60000/0C9D8401-64F6-E711-AB87-FA163EA2324A.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/20001/908A6CA2-B801-E811-BF3F-A4BF0112F6B0.root',
] )
