import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/50000/A69590E1-4CE4-E711-8AFA-001A649D4AE1.root',
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/60001/DC8DD206-9CEB-E711-80BE-001E67DDBFF7.root',
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/60001/4A1E28BA-9EEB-E711-85A1-0CC47A5FA215.root',
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/60000/B40E77FB-CDE5-E711-B332-141877636851.root',
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/60001/E23A35D3-C3EB-E711-87FC-141877410EC1.root',
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/60002/A8D96644-1FED-E711-AEFE-1866DA85DEA3.root',
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/60001/E2ACDE61-5FEC-E711-B8B9-0CC47A1DF82E.root',
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/60001/347EBEFF-5EEC-E711-AF54-0CC47A1DF7FC.root',
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/60002/52AC18D1-55EC-E711-ADF0-0CC47A1DF620.root',
#       '/store/data/Run2017B/MET/AOD/17Nov2017-v1/60000/DA007236-36E4-E711-AB94-B083FED045EC.root',
] )
