import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016D/MET/AOD/07Aug17-v1/110000/642778BC-0899-E711-B10C-7CD30ACE11E6.root',
       '/store/data/Run2016D/MET/AOD/07Aug17-v1/110000/76E91212-7C98-E711-9BDE-10983627C3C1.root',
       '/store/data/Run2016D/MET/AOD/07Aug17-v1/10000/1645BCD2-5B99-E711-BD44-002481CFD184.root',
] )
