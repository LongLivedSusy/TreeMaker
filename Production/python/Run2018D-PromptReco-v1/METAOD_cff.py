import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/data/Run2018D/MET/AOD/PromptReco-v1/000/320/413/00000/18D24C8B-5693-E811-830E-FA163E29F8F6.root',
#'/store/data/Run2018D/MET/AOD/PromptReco-v1/000/320/416/00000/2CAF4E31-5993-E811-BD93-FA163E9CD516.root',
#'/store/data/Run2018D/MET/AOD/PromptReco-v1/000/320/434/00000/7A7FD8E7-BD93-E811-992A-FA163E196AC6.root',
] )











