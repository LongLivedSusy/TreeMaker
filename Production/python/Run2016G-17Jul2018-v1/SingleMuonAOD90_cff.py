import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00003/D417A9B7-15AF-E711-B777-008CFAFC04AC.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00000/E0EF6651-DFAE-E711-9FC1-0025905A60E4.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00000/B607EB18-D3AE-E711-8E66-7CD30ACE19D8.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00003/C8F86CEE-1DAF-E711-A7EC-FA163E6A32B0.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/110000/0A808B70-8196-E711-8E14-0026B927866B.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00002/10B5A1D0-0CAF-E711-B5A5-0CC47A7C3458.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00004/F0745ABA-2EAF-E711-8C1D-02163E00F786.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00002/5CA05ACD-01AF-E711-96A8-0025905A48D6.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00002/72C2444B-07AF-E711-A4B0-02163E00C2A7.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00004/889D41A9-3DAF-E711-9214-0025905A60CE.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00002/5690F76A-0FAF-E711-BD25-02163E013FA0.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00002/5250754A-14AF-E711-BA3A-02163E016497.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00002/5690F76A-0FAF-E711-BD25-02163E013FA0.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/110001/5E40CBC2-AB98-E711-BF74-A4BF0112BD44.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/10000/006BDBC9-C996-E711-BB94-001E677925AC.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/110001/A4E6E854-9C98-E711-9DBC-00259073E496.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/110000/F61468C2-2F98-E711-AAA4-00259073E4CC.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/110000/3A56EB7B-BF8C-E711-AB3A-009C02AAB554.root',
#       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/90000/AAAC3B97-798C-E711-B6F6-0026B94DBE0A.root',
] )
