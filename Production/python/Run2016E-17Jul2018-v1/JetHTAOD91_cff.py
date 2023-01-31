import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016E/JetHT/AOD/07Aug17-v1/70000/F4F086AA-BC89-E711-A07C-0025905B8586.root',
       '/store/data/Run2016E/JetHT/AOD/07Aug17-v1/110000/9ED0B02D-CC89-E711-8347-0025905A605E.root',
] )
