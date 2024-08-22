import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018B/JetHT/AOD/17Sep2018-v1/120000/4627F31D-829D-8B43-A0D4-4D49CE7602A2.root',
       '/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/19C4813E-2C52-574C-B905-B60F6E144CAA.root',
       '/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/1692C93A-418E-5549-BCD7-20B8C1612CBA.root',
       '/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/78E69E65-73AD-4946-BE21-ED3E07F3E3C9.root',
       '/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/00000/D076F460-1ACC-2B41-A3DE-1DAAC895598F.root',
] )
