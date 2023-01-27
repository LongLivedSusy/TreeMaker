import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/110001/5CC0A57C-2486-E711-BCE8-0CC47A4D767E.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/70000/0E79968A-0B81-E711-86BA-0025905B8612.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/110000/2AA63FE5-8181-E711-B9A5-24BE05C64601.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/70002/CEEFEC2D-2082-E711-8A3D-0CC47A7C3412.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50002/BAEBCC9D-4282-E711-83DB-0CC47A4D75F6.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50000/4AAA7257-6381-E711-A151-003048FFD75A.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50000/7EF3B41A-9081-E711-9D18-0025905A6080.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/70001/946824F7-2B82-E711-8A6F-0025905A607A.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50002/484DCCB5-8B82-E711-94B2-0CC47A7C347E.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50000/00528D22-9D81-E711-84C8-002590E2DA08.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50000/9A92D476-3181-E711-A508-0025905B85AE.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/110001/1EAC597D-CC85-E711-9E91-0025905B85D0.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/70001/58080AFB-1582-E711-A42F-0025905A607A.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50002/882F2374-6D82-E711-8642-0CC47A4C8F26.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50002/8A852995-6B82-E711-A44A-0025905B85FC.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50002/882F2374-6D82-E711-8642-0CC47A4C8F26.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50002/8A852995-6B82-E711-A44A-0025905B85FC.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50000/682B1FD1-A781-E711-8119-0025905B85F6.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/70000/EC5BD7A5-8E81-E711-B31B-0025905B85D8.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/110002/18AACDDF-2E87-E711-A88E-0CC47A4C8EB6.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/70000/D2A099F8-A881-E711-B534-0025905B85D2.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/70000/6091B24E-B181-E711-B33B-0025905B85DC.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/70000/D2A099F8-A881-E711-B534-0025905B85D2.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/70000/6091B24E-B181-E711-B33B-0025905B85DC.root',
#       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/50001/EC29BE12-EA81-E711-80AE-0025905A60B4.root',
] )
