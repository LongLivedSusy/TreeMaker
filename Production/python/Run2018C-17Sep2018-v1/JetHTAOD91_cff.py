import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2018C/JetHT/AOD/17Sep2018-v1/00001/3A843148-24F2-E046-A3D4-10709D624297.root',
#       '/store/data/Run2018C/JetHT/AOD/17Sep2018-v1/270000/83A3F9A5-F71C-0C47-922C-2605AF22742B.root',
#       '/store/data/Run2018C/JetHT/AOD/17Sep2018-v1/00002/BA615DB8-B8B2-0B47-80A7-F2C0479E7D4B.root',
] )
