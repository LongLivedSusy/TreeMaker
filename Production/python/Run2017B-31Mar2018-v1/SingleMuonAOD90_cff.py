import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/60007/3E663ED6-16D8-E711-8DB9-02163E011ED6.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/60002/22E16F8C-F3D7-E711-BAF6-02163E019DF7.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/70000/DE40A7B6-5DD7-E711-A9A2-B083FED0FFCF.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/70001/F489B4EF-DFD7-E711-899A-02163E019CB1.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/70001/6460802A-E3D7-E711-AD72-02163E01A1D0.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/70000/6EC09B9E-C1D7-E711-9823-02163E019BF7.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/72E045CF-ADD8-E711-A321-002590E7DFE0.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/08FD2947-63D8-E711-9AC9-0CC47A1E0DBC.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/70003/C05395D5-91D8-E711-952E-02163E019B83.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/60002/501253D0-2BD8-E711-B207-0425C5DE7BF6.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/60001/3E331517-F1D7-E711-913D-02163E019BEF.root',
#       '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/C6CB9A34-5FD8-E711-9980-0425C5DE7BEC.root',
] )
