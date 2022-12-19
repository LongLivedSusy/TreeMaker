import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/10002/045D86D9-2B01-E811-8B4E-F4E9D497BBE0.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/10003/C42C1B7A-3D02-E811-B24C-0CC47A1E0DC8.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/00002/B01BDACD-6BFF-E711-AE8A-1866DA7F8F0C.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/10001/A6FA4F5B-0CFF-E711-98D3-0CC47A1DF808.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/20000/94A0F161-0501-E811-AA28-0242AC130002.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/80001/0666431E-7CFE-E711-A3CE-A4BF01125AD0.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/00000/9069602D-18FE-E711-A2B9-24BE05C68671.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/10002/061D4C18-6001-E811-A073-B499BAAC054A.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/10002/0CD57DAE-5C01-E811-949D-02163E01A51E.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/00002/EE805EB5-43FF-E711-9F16-1866DAEA79D4.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/00001/D89F9A1F-0DFF-E711-9BB5-801844DEE0E0.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/00002/EE805EB5-43FF-E711-9F16-1866DAEA79D4.root',
       '/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/10000/9EB33493-7FFF-E711-80F7-A4BF01125418.root',
] )
