import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/00000/DA340842-24F8-E711-A4B1-A4BF0112BDF0.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/80000/98C6D805-FDF9-E711-B15B-002590200A58.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/70000/34DF3B29-57F6-E711-B6F5-C4346BC8E730.root',
       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/80000/2048F47D-86FB-E711-B622-0242AC1C0501.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/80000/20FB6A1E-0EFA-E711-96BC-A4BF010F0F08.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/80000/9632C10D-6AFB-E711-802F-0242AC1C0500.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/10001/CEDDD4C8-44FB-E711-BDC5-A4BF011256C0.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/70000/069D61E7-C6F9-E711-9DA6-F04DA275BFCE.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/20001/6EC68CE1-F301-E811-9AED-008CFA05206C.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/20001/AE724FC7-D701-E811-9BFB-AC162DACC328.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/60001/24C1AC2E-2BF8-E711-A0CE-A4BF0112BC58.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/10002/D2E92C72-E8FA-E711-ACFF-0242AC1C0500.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/00000/082A05AB-88F6-E711-B1E0-A4BF0112E310.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/20000/28BBDB9A-30FA-E711-93C6-A0369F83635A.root',
#       '/store/data/Run2017E/SingleElectron/AOD/17Nov2017-v1/70000/A24EB7BD-D4F9-E711-849A-A0369F836430.root',
] )
