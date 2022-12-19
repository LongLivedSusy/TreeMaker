import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016E/SingleElectron/AOD/07Aug17-v1/50001/C0DA38DE-8999-E711-805E-00259074AE52.root',
       '/store/data/Run2016E/SingleElectron/AOD/07Aug17-v1/710000/8C8F5D91-429C-E711-864F-02163E019BEA.root',
       '/store/data/Run2016E/SingleElectron/AOD/07Aug17-v1/10000/3E19B050-8D95-E711-8681-0CC47A1DF81E.root',
       '/store/data/Run2016E/SingleElectron/AOD/07Aug17-v1/710000/EE59C60F-3E9C-E711-9ECC-02163E01A583.root',
       '/store/data/Run2016E/SingleElectron/AOD/07Aug17-v1/10000/887C3DCA-7B93-E711-BE85-0242AC110003.root',
] )
