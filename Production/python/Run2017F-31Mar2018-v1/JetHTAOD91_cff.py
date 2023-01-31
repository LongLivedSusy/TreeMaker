import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70004/50F7A52E-BDE2-E711-B4E4-0025905B8568.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70001/2E2387B3-5FDF-E711-819F-001E67E33C60.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70004/02A83803-28E0-E711-A22A-02163E011DE5.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/70003/EE6D1C25-55E2-E711-A2CA-0025905B8564.root',
       '/store/data/Run2017F/JetHT/AOD/17Nov2017-v1/60000/18ACAF72-40E0-E711-B524-008CFAFC04AC.root',
] )
