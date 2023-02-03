import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/40004/4CCE6398-17D9-E711-9C34-02163E01A5C6.root',
#       '/store/data/Run2017C/SingleMuon/AOD/17Nov2017-v1/50000/9A7DD06E-17DA-E711-BBE7-02163E011F84.root',
] )
