import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017D/MET/AOD/17Nov2017-v1/50000/6C524C84-BAE5-E711-91D3-0CC47A4D76D2.root',
#       '/store/data/Run2017D/MET/AOD/17Nov2017-v1/70000/96AE026D-E1E4-E711-A4B2-0CC47A1E0748.root',
#       '/store/data/Run2017D/MET/AOD/17Nov2017-v1/50000/20F2F39F-25EB-E711-87BC-0025907254D4.root',
#       '/store/data/Run2017D/MET/AOD/17Nov2017-v1/60000/9A5C2547-94EC-E711-B2FE-0CC47A13D2A4.root',
] )
