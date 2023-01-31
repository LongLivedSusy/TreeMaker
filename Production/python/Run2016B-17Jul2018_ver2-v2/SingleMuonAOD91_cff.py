import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/110001/5CC0A57C-2486-E711-BCE8-0CC47A4D767E.root',
       '/store/data/Run2016B/SingleMuon/AOD/07Aug17_ver2-v1/110001/1EAC597D-CC85-E711-9E91-0025905B85D0.root',
] )
