import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2018D/JetHT/AOD/PromptReco-v1/000/320/434/00000/885FDC69-BD93-E811-BAE5-FA163E30DE9F.root',
'/store/data/Run2018D/JetHT/AOD/PromptReco-v1/000/320/434/00000/A03212F4-BC93-E811-AF9F-02163E010C23.root',
#'/store/data/Run2018D/JetHT/AOD/PromptReco-v1/000/320/413/00000/A4EA6DCB-5593-E811-AC52-FA163E19BDBB.root',
#'/store/data/Run2018D/JetHT/AOD/PromptReco-v1/000/320/416/00000/9E327703-5A93-E811-B036-02163E00BC72.root',
] )



























