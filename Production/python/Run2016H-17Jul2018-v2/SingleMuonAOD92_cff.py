import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70001/5C23F46F-6780-E711-B4E3-0090FA9DFD7A.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/76B20148-A680-E711-AD1C-0090FAA581E4.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/984440A6-AA80-E711-A1F0-48FD8EE73ABD.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/A8646A50-B080-E711-95D9-00259073E4EA.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70001/80E945F2-7680-E711-B834-F02FA768CD88.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/6E3F6602-9480-E711-B35A-0CC47A4DEDF0.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/3CA76380-A180-E711-8FB3-0090FAA58B64.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/32752585-8F80-E711-84A5-48FD8E28296F.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/50001/029D92F2-AD80-E711-AD65-7CD30AD095BC.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70001/1AE1CC3B-5B80-E711-9082-0025907B4E6C.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70001/A6771CE5-7680-E711-B372-48FD8EE73A8B.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/DAB6B2DA-9080-E711-979D-0025907B4F24.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/1C622081-9E80-E711-A862-00259073E31C.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/106D10F8-7E80-E711-9763-48D539F38882.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/C6066F17-BB80-E711-B2AD-00259073E34E.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/12B4ABFE-9380-E711-B638-0090FAA57420.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/B49ED5B8-7D80-E711-8080-48FD8EE73A01.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70001/C8A2A592-6180-E711-9F90-002590D0B0AE.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/3A96CED3-8780-E711-B1EB-002590D0AFC8.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/748E8D01-BE80-E711-8B55-002590D0B030.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/76C73F64-B980-E711-AD7F-0CC47A4D99F0.root',
       '/store/data/Run2016H/SingleMuon/AOD/07Aug17-v1/70002/1CBF424D-9980-E711-BA19-0090FAA59EE4.root',
] )
