import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/50000/E458DB87-F2DD-E711-AA37-02163E019E83.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70000/4AEB8D0C-09DE-E711-B76D-02163E01347A.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/60000/F8ED2704-86E2-E711-964E-02163E019B9C.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/40000/C0EC07D4-D9DB-E711-A2FA-02163E01A2D1.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/60000/24046F68-54E0-E711-A3F2-D4856444779A.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/60000/34EDDE47-0BE1-E711-A5C6-984BE16440FC.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/40000/78D54E40-EADB-E711-8940-02163E01A56D.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/40000/F4B4848C-EEDB-E711-9BB1-02163E0122FE.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/60001/04FB3859-23E4-E711-8D60-02163E01A1E6.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/60001/EA8ECB1C-26E4-E711-9C46-02163E01356F.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70000/7AA769D1-08DE-E711-9876-02163E01A2E7.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/60000/58D0675C-97E2-E711-A9E6-02163E019D1E.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70000/001A22EE-C1DE-E711-84EA-FA163EC4E221.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70001/78C69E02-C1DE-E711-857E-FA163E6659D1.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/70000/001A22EE-C1DE-E711-84EA-FA163EC4E221.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/60001/745128BC-28E4-E711-811F-00215A4909F6.root',
#       '/store/data/Run2017B/SingleElectron/AOD/17Nov2017-v1/60001/908CAF92-1EE4-E711-9EBF-02163E01A580.root',
] )
