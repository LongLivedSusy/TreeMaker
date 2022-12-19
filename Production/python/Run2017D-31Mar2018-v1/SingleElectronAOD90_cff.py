import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017D/SingleElectron/AOD/17Nov2017-v1/70001/685B8CF1-81DA-E711-8638-008CFAE45064.root',
       '/store/data/Run2017D/SingleElectron/AOD/17Nov2017-v1/50000/066EBDE2-A0D9-E711-A9E6-44A842CFD633.root',
       '/store/data/Run2017D/SingleElectron/AOD/17Nov2017-v1/70001/8C9D65ED-71DC-E711-B220-0CC47A13D2A4.root',
       '/store/data/Run2017D/SingleElectron/AOD/17Nov2017-v1/60000/02E1074A-0CDA-E711-85CA-FA163E65B484.root',
] )
