import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2016C/MET/AOD/07Aug17-v1/110000/8AC64880-219A-E711-92D9-A4BF0101DDD7.root',
#       '/store/data/Run2016C/MET/AOD/07Aug17-v1/110000/16965FCF-E799-E711-B5AE-E0071B7AC7C0.root',
#       '/store/data/Run2016C/MET/AOD/07Aug17-v1/110000/7AA40992-449A-E711-8F87-60EB69BAC87C.root',
#       '/store/data/Run2016C/MET/AOD/07Aug17-v1/110000/46A86DD3-1F9A-E711-9AF7-0242AC130002.root',
] )
