import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/SingleMuon/AOD/07Aug17-v1/70000/9E9487A3-5081-E711-8066-6C3BE5B581A8.root',
       '/store/data/Run2016C/SingleMuon/AOD/07Aug17-v1/70000/FA33659F-5D81-E711-BFE1-001F290789D6.root',
       '/store/data/Run2016C/SingleMuon/AOD/07Aug17-v1/50000/4863A9FA-8D7F-E711-A0E9-001F2908BE72.root',
       '/store/data/Run2016C/SingleMuon/AOD/07Aug17-v1/70001/9EC5094F-0F82-E711-A31F-008CFA1C907C.root',
       '/store/data/Run2016C/SingleMuon/AOD/07Aug17-v1/110000/42FA1E54-EC7F-E711-B433-001E67398E49.root',
       '/store/data/Run2016C/SingleMuon/AOD/07Aug17-v1/50000/BA1206E4-438A-E711-BA29-008CFA0A58B8.root',
       '/store/data/Run2016C/SingleMuon/AOD/07Aug17-v1/70000/484442C5-1081-E711-98AE-6C3BE5B5B340.root',
       '/store/data/Run2016C/SingleMuon/AOD/07Aug17-v1/50000/B24B9F49-BA7F-E711-A7D3-549F358EB76F.root',
       '/store/data/Run2016C/SingleMuon/AOD/07Aug17-v1/70000/D6F8E953-BC7F-E711-A126-D8D385B0EE2E.root',
] )
