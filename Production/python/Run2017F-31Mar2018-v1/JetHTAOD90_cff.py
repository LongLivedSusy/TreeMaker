import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/50002/200BF922-03E0-E711-8D7B-0025905B8574.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/50000/F0296311-D1DE-E711-815A-02163E019DD8.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70003/EE6D1C25-55E2-E711-A2CA-0025905B8564.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70004/02A83803-28E0-E711-A22A-02163E011DE5.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/50000/3C57BFC2-A4DE-E711-99A5-002590200A80.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/50002/12790B38-C2DF-E711-9BD5-02163E014507.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/50001/56835C3A-94DF-E711-9079-001E67E6F8D7.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70003/684D4F41-CAE2-E711-A001-0CC47A7C35F8.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70004/50F7A52E-BDE2-E711-B4E4-0025905B8568.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/60000/18ACAF72-40E0-E711-B524-008CFAFC04AC.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/60003/EC86AFA9-8BE1-E711-8A52-02163E01A445.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70001/A048348D-64DF-E711-AAEB-02163E0145B1.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/60001/4628AF50-5EE0-E711-BF50-02163E014748.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70000/AEB9BD16-46DF-E711-8006-FA163E3FAC87.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70002/E6BC40B7-A5DF-E711-8DC7-FA163E740D18.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70000/AEB9BD16-46DF-E711-8006-FA163E3FAC87.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70001/2E2387B3-5FDF-E711-819F-001E67E33C60.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70001/3E1A55B3-94DF-E711-909B-02163E0143B7.root',
#       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/60001/E2780C62-7BE0-E711-BC41-484D7E8DF0D3.root',
] )
