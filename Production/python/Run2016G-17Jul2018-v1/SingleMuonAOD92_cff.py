import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00002/380C6860-00AF-E711-BD04-008CFAFBEC34.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00003/845F69DB-20AF-E711-9045-FA163E93DA5C.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/710000/DAF1C7C8-E9A2-E711-B9F4-02163E01A783.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00004/D2975659-34AF-E711-9321-FA163E874178.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/710000/E8DB3A17-EAA2-E711-987A-02163E019B5C.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/710000/443A25BE-E9A2-E711-B28E-02163E01348F.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/010000/AA7AD545-CFB1-E711-B188-3417EBE2F4CC.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00003/7CF7CF7F-17AF-E711-A065-0025905A60EE.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/710000/FADBAD28-EAA2-E711-87EB-02163E01A752.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/010000/EC9C95E5-CEB1-E711-838E-3417EBE65E39.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/010000/76A7BFE7-EBB0-E711-BF47-3417EBE64519.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/00003/8E67AD2D-1EAF-E711-A3B1-0CC47A4C8E28.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/710000/F83064BB-E9A2-E711-86DA-02163E01A295.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/710000/80BE1BD0-E9A2-E711-A86E-02163E01415A.root',
       '/store/data/Run2016G/SingleMuon/AOD/07Aug17-v1/010000/A4D996BB-EAB0-E711-B4F8-3417EBE64444.root',
] )
