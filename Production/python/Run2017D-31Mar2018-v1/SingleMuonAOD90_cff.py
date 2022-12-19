import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/50000/C4B86DFE-BFE0-E711-9080-0026B94DBD7B.root',
       '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/60000/B61C016A-FBE1-E711-A5E3-008CFAF292B2.root',
       '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/70001/F43488BE-26E4-E711-B564-7845C4FC363E.root',
       '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/70001/5E681530-26E4-E711-8A03-3417EBE644BF.root',
       '/store/data/Run2017D/SingleMuon/AOD/17Nov2017-v1/60000/CE05BC2F-3DD8-E711-96F4-A0369F6367C2.root',
] )
