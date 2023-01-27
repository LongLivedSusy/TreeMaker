import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2016D/SingleMuon/AOD/07Aug17-v1/10000/60A4179C-4F8C-E711-906C-009C02AAB258.root',
#       '/store/data/Run2016D/SingleMuon/AOD/07Aug17-v1/90000/8CF92A14-038B-E711-A535-0242AC110011.root',
#       '/store/data/Run2016D/SingleMuon/AOD/07Aug17-v1/90000/043A42DB-AD8A-E711-9A1D-0242AC110009.root',
#       '/store/data/Run2016D/SingleMuon/AOD/07Aug17-v1/110000/48CC9A71-C797-E711-8B4A-7CD30AD089E0.root',
#       '/store/data/Run2016D/SingleMuon/AOD/07Aug17-v1/50000/2027A63C-AB8C-E711-9E3B-F02FA768CCD8.root',
#       '/store/data/Run2016D/SingleMuon/AOD/07Aug17-v1/90001/B626072B-5D8C-E711-9C77-002590D0B00C.root',
#       '/store/data/Run2016D/SingleMuon/AOD/07Aug17-v1/90000/A87B1CB4-0E8C-E711-9EB4-48D539F38894.root',
#       '/store/data/Run2016D/SingleMuon/AOD/07Aug17-v1/90000/0EF4AABD-4386-E711-95D1-3417EBE520A5.root',
#       '/store/data/Run2016D/SingleMuon/AOD/07Aug17-v1/10000/08F10BAA-718C-E711-8EDD-7845C4FC3C7D.root',
] )
