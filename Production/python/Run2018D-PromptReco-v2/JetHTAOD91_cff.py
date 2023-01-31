import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/325/170/00000/B48535E8-E1ED-B64E-BE7E-4C336DB28B9E.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/324/835/00000/C35113CF-A3E6-994D-817A-515D06975206.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/325/057/00000/CA286476-DA00-FE4B-9146-9CA609C60CC3.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/325/057/00000/98ECA44B-CF0F-0B41-AE6C-F05056AE4C9B.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/324/791/00000/879ED37F-DD45-AD47-8DA3-5E3DF176AC34.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/324/835/00000/4F8C8EEA-B96F-D245-9C18-EE33839D4650.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/324/835/00000/93A628EE-3252-1E43-9989-2CEBA5C672F7.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/324/835/00000/FD785FCD-F83F-264A-A8F7-B91F0EB38CD8.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/321/475/00000/A8AB759F-5BA6-E811-AF9B-FA163E188988.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/320/936/00000/663A4D26-339C-E811-8F04-FA163EEE21BE.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/321/069/00000/84510500-249E-E811-81BC-02163E019FC5.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/324/835/00000/3311CDFA-2AA0-A040-A4F2-D8AEB243EF49.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/324/835/00000/DB6A1CB2-6120-834F-B520-61AA890A3C51.root',
       '/store/data/Run2018D/JetHT/AOD/PromptReco-v2/000/324/835/00000/24C1C228-4501-9647-8739-6D8F7D18C49D.root',
] )
