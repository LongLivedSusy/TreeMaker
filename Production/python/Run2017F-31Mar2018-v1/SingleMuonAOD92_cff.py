import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70002/6C7AFA8B-95E1-E711-9976-001517FB141C.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70002/66A3E847-A0E1-E711-A0C8-001E67A3EC2D.root',
       '/store/data/Run2017F/SingleMuon/AOD/17Nov2017-v1/70003/40D7598B-5BE1-E711-B122-001E67A40523.root',
] )
