import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2016D/SingleElectron/AOD/07Aug17-v1/90002/0C01CF58-348A-E711-8D84-1866DA890B10.root',
#       '/store/data/Run2016D/SingleElectron/AOD/07Aug17-v1/90000/30FCE5A5-FA86-E711-9749-0CC47A7FC72C.root',
#       '/store/data/Run2016D/SingleElectron/AOD/07Aug17-v1/50000/B0C4949C-3A86-E711-AA85-002590D8C7E2.root',
#       '/store/data/Run2016D/SingleElectron/AOD/07Aug17-v1/50000/7C933322-8E87-E711-8A66-0CC47A4C8EE2.root',
#       '/store/data/Run2016D/SingleElectron/AOD/07Aug17-v1/90000/E6CBAEA2-3C86-E711-B8E4-008CFA14FA8C.root',
       '/store/data/Run2016D/SingleElectron/AOD/07Aug17-v1/70000/E2C21F27-B886-E711-B6B5-0CC47A7FC6E6.root',
#       '/store/data/Run2016D/SingleElectron/AOD/07Aug17-v1/90002/84FF6EE6-E089-E711-9D42-FA163E1AB9FF.root',
#       '/store/data/Run2016D/SingleElectron/AOD/07Aug17-v1/90003/2098D627-588A-E711-8A04-1458D04903A8.root',
] )
