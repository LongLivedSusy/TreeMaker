import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/50000/DA549BCC-22DF-E711-9227-0025905A6134.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70003/F84CAD45-6AE2-E711-856F-0CC47AA53D8A.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70004/2AFD601D-79E8-E711-9044-0CC47A6C1058.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70006/289E5CF5-DCDF-E711-8E51-02163E011AA4.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70006/324EF1AA-5FE0-E711-8120-02163E01373B.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/60001/980DC930-B5E4-E711-ACC9-0CC47A4C8E22.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/60006/9C1AEE79-86E9-E711-A026-008CFAC91508.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/60007/90B7AEA2-43E4-E711-8AC9-0CC47A4D76A0.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70010/2AB511F2-61E0-E711-811E-1CB72C0A3DC1.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/60008/681195D3-7AE6-E711-88FA-008CFAC93C30.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/50016/AAE9DF0E-37E4-E711-BC33-1866DA85DC53.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70014/7E355F2A-30E0-E711-BD50-0CC47A4C8E46.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70005/44239DD0-E8E9-E711-B8C8-0CC47A57CC42.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/50001/BCC42F05-EADF-E711-8E66-02163E012B43.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/50002/C861130C-F7DF-E711-BBE4-1866DA89095D.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70001/007631CB-80E1-E711-93D1-001E675A6630.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/50001/762B7EA2-5AE0-E711-809F-02163E01A6B6.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/50001/70BFBC0D-F1DF-E711-BB65-02163E019E35.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/50001/762B7EA2-5AE0-E711-809F-02163E01A6B6.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/60000/6C924F7C-4CE1-E711-A670-008CFAC919F8.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70003/686F6220-89E2-E711-82D5-008CFAC91678.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/60010/5E091355-29EB-E711-A398-008CFAE4546C.root',
] )
