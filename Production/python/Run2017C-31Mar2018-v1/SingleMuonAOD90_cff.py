import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40004/C007B38A-78D9-E711-96B9-02163E01A6C9.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40003/AA886C37-CBD8-E711-B285-02163E01462B.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40003/1AACA611-BAD8-E711-A3C0-02163E01A451.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40000/2E945C17-90D7-E711-AA1D-02163E019C3A.root',
       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/50000/A648E890-24DA-E711-8856-02163E01285A.root',
       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/50000/9A7DD06E-17DA-E711-BBE7-02163E011F84.root',
       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/50000/A648E890-24DA-E711-8856-02163E01285A.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40003/58C7F25C-E7D8-E711-86C0-02163E01A39F.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40003/9C06B2F4-A8D8-E711-BB67-1CB72C1B6C32.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40003/9C06B2F4-A8D8-E711-BB67-1CB72C1B6C32.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40005/2AE25633-14DA-E711-ABAD-02163E014685.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/60002/4E403BBB-DFD9-E711-822F-02163E019CAF.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/50001/F615A2A5-A6DA-E711-903A-02163E011A55.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/50001/90217B3C-9BDA-E711-8304-02163E01317C.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40001/58312BAD-F5D7-E711-8FD6-02163E019CB8.root',
       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40004/E62A2A8D-15D9-E711-93F8-02163E019E8B.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40004/4CCE6398-17D9-E711-9C34-02163E01A5C6.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/60000/108A4E43-49D8-E711-9CA9-02163E019DA2.root',
] )
