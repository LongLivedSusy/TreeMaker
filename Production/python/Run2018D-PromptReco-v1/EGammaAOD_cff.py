import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2018D/EGamma/AOD/PromptReco-v1/000/320/413/00000/2A622BB1-5593-E811-845D-FA163E1302C1.root',
'/store/data/Run2018D/EGamma/AOD/PromptReco-v1/000/320/434/00000/32D79DF0-BC93-E811-8714-FA163EFA38D9.root',
'/store/data/Run2018D/EGamma/AOD/PromptReco-v1/000/320/434/00000/966E12EA-BC93-E811-9D72-02163E00CDCE.root',
'/store/data/Run2018D/EGamma/AOD/PromptReco-v1/000/320/416/00000/7001A75C-5893-E811-9386-FA163EFCC9EE.root',
] )




