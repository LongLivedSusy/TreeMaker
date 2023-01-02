import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/JetHT/AOD/07Aug17-v1/50001/6822439E-DD7C-E711-B720-0CC47A13CFC0.root',
       '/store/data/Run2016C/JetHT/AOD/07Aug17-v1/110000/A8BF29FE-FA7C-E711-8B6A-0CC47A78A3F8.root',
       '/store/data/Run2016C/JetHT/AOD/07Aug17-v1/70001/5A4A71C7-397D-E711-9529-0025905B860C.root',
#       '/store/data/Run2016C/JetHT/AOD/07Aug17-v1/70000/CE909607-847C-E711-A8A0-0242AC130002.root',
       '/store/data/Run2016C/JetHT/AOD/07Aug17-v1/70000/70ADDB87-DC7C-E711-9227-0CC47A537688.root',
#       '/store/data/Run2016C/JetHT/AOD/07Aug17-v1/70000/CE909607-847C-E711-A8A0-0242AC130002.root',
       '/store/data/Run2016C/JetHT/AOD/07Aug17-v1/70000/70ADDB87-DC7C-E711-9227-0CC47A537688.root',
#       '/store/data/Run2016C/JetHT/AOD/07Aug17-v1/70000/CE909607-847C-E711-A8A0-0242AC130002.root',
       '/store/data/Run2016C/JetHT/AOD/07Aug17-v1/70000/70ADDB87-DC7C-E711-9227-0CC47A537688.root',
] )
