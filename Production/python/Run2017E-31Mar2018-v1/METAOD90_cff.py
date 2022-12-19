import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017E/MET/AOD/17Nov2017-v1/70000/9078F739-E6DC-E711-8BF4-02163E019C0B.root',
       '/store/data/Run2017E/MET/AOD/17Nov2017-v1/70002/8292EB0B-38E1-E711-954A-02163E0144D3.root',
       '/store/data/Run2017E/MET/AOD/17Nov2017-v1/50001/42885D5B-ACDC-E711-8B5E-02163E0144E1.root',
       '/store/data/Run2017E/MET/AOD/17Nov2017-v1/60005/CE271F06-C4E1-E711-B4D2-02163E0140F7.root',
       '/store/data/Run2017E/MET/AOD/17Nov2017-v1/50000/EC5FB40E-FDE1-E711-8F1E-02163E01347D.root',
       '/store/data/Run2017E/MET/AOD/17Nov2017-v1/60002/06FDFBF8-50DC-E711-BCA7-02163E014318.root',
       '/store/data/Run2017E/MET/AOD/17Nov2017-v1/70000/083C1EE9-EDDC-E711-9C09-02163E019BF5.root',
       '/store/data/Run2017E/MET/AOD/17Nov2017-v1/70001/306AF01C-92E1-E711-9C19-F01FAFD68FC8.root',
       '/store/data/Run2017E/MET/AOD/17Nov2017-v1/50000/1839ADA7-ACDC-E711-BF1D-02163E01370A.root',
] )
