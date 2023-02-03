import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70001/5E749CA6-45DE-E711-B0A1-02163E0143BC.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70000/5823EA79-4EDE-E711-AE48-02163E019CA0.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70000/9859EE55-8FDD-E711-AA79-02163E014245.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70000/54FDC820-94DD-E711-B6EF-02163E01A450.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70001/E07D5504-C1DE-E711-91B8-FA163E5EBCED.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70000/F29B264A-94DD-E711-A74E-02163E019BA9.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/60001/947E2B8F-23E4-E711-BAC5-02163E019E0E.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/40000/6631B21A-94DC-E711-8BD5-0017A4770C4C.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70001/3AA145A4-45DE-E711-90B9-02163E014168.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70000/165C2386-4EDE-E711-B45D-02163E01A1B7.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70001/32F56BF6-DFDE-E711-B965-441EA1616D3A.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70001/F043880A-C1DE-E711-A403-FA163E714FAE.root',
] )
