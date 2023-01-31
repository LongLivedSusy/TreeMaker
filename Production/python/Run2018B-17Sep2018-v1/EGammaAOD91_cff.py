import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018B/EGamma/AOD/17Sep2018-v1/100002/94C08486-1C7C-8949-81D6-FC8B44EA343E.root',
       '/store/data/Run2018B/EGamma/AOD/17Sep2018-v1/100002/3A5D42E0-D59F-F94A-A11A-88D70B038704.root',
] )
