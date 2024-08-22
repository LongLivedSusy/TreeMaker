import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50001/6E684D42-9F7F-E711-80FE-0CC47A7C3424.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50001/A04A84B8-A67F-E711-809F-0025905A4964.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50001/2249ABC3-A37F-E711-81C1-0025905A4964.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50002/E2C298C6-2D80-E711-9679-0CC47A78A4A0.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50003/78A13BF9-1580-E711-835A-0CC47A4C8E56.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50003/706A232C-0880-E711-A7E5-0025905A6068.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50002/A61F8768-2280-E711-A820-0025905B8574.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50002/CC51AD97-1F80-E711-B0F4-0025905B8612.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50002/D441E1A8-FB7F-E711-B948-0CC47A78A4B0.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50002/1C75AEC4-0080-E711-AF62-0CC47A78A2F6.root',
       '/store/data/Run2016E/SingleMuon/AOD/07Aug17-v1/50002/5692D2CE-F87F-E711-822B-0CC47A78A33E.root',
] )
