import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50002/A216362F-A4E0-E711-9261-1866DAEEB358.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50003/304B314B-F7E0-E711-A2E4-FA163EB330ED.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/60000/1607D64B-1BDF-E711-979A-6C3BE5B59150.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/60000/1EF187E4-10DF-E711-A60E-001F2908F0E4.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50000/92B77C66-3EE2-E711-969B-0025905B8560.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50002/C06CEFB2-93E0-E711-87C4-0CC47AD99050.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/70001/123092CC-2AE1-E711-BA58-FA163E185B6E.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50002/DEE6080C-DEE0-E711-92D0-5065F382A241.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50002/F277C297-99E0-E711-B397-0242AC130002.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50002/8AB947DB-DDE0-E711-AC9B-FA163E85E28C.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/60001/9CBD694B-78DF-E711-A51B-001E67E6F4FE.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50001/D4107DAC-48E2-E711-BD06-0CC47A7C345E.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50003/FAEA4676-06E1-E711-8566-003048CB7A8A.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/50003/B4A7954B-FDE0-E711-B6AA-0CC47A57CB8E.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/60003/E245ADB2-76E0-E711-920C-FA163EF00E59.root',
#       '/store/data/Run2017F/SingleElectron/AOD/17Nov2017-v1/60004/DE1B5C2F-9BE1-E711-BD5E-0025905B861C.root',
] )
