import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018D/MET/AOD/PromptReco-v2/000/320/822/00000/704B885B-AA99-E811-81B6-FA163E03A9B7.root',
       '/store/data/Run2018D/MET/AOD/PromptReco-v2/000/324/980/00000/9904B13B-E4F5-FD44-AB4F-DBA1D5FC1207.root',
       '/store/data/Run2018D/MET/AOD/PromptReco-v2/000/322/602/00000/2664483E-9CB8-E811-ADC8-FA163E8D8332.root',
       '/store/data/Run2018D/MET/AOD/PromptReco-v2/000/321/917/00000/E6D03BDB-BBAE-E811-98BB-FA163E2AABBC.root',
       '/store/data/Run2018D/MET/AOD/PromptReco-v2/000/324/318/00000/8959C45D-BD49-4A43-8C75-9391963EE992.root',
       '/store/data/Run2018D/MET/AOD/PromptReco-v2/000/322/106/00000/8A4F4D44-9DB2-E811-ACD9-FA163EB0ADBE.root',
       '/store/data/Run2018D/MET/AOD/PromptReco-v2/000/321/414/00000/8E84A6AF-80A4-E811-AC5D-FA163EAAF8B5.root',
       '/store/data/Run2018D/MET/AOD/PromptReco-v2/000/322/381/00000/0038FC3E-BBB4-E811-8E21-02163E01A06F.root',
] )
