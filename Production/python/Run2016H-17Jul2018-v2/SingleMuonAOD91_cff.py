import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/50001/1ADEF49A-A480-E711-B28D-7845C4FC3C4D.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/2816E637-8080-E711-AD24-0090FAA58C74.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/50002/C4354C44-C481-E711-9924-7845C4FC3A61.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70001/E23EB947-6F80-E711-BF74-48FD8EE73A01.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/FAAC33CA-9B80-E711-A323-F02FA768CB64.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/50001/08FFF91A-9880-E711-8BBA-3417EBE2EC95.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70000/74322608-FE7F-E711-9278-0CC47A4C8EA8.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/110000/FCB06F06-7880-E711-AB51-203DB23FCB7E.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/50001/B4103BD2-9B80-E711-BA4F-7845C4FC3BFF.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70001/0EE6DEA6-7B80-E711-9965-0CC47A4DEDB8.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/A603627D-B780-E711-8F64-0090FAA58124.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70003/0ECF0076-9686-E711-A9A1-48FD8EE73AF5.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/50001/C645FF8A-A080-E711-BCB4-3417EBE338FA.root',
] )
