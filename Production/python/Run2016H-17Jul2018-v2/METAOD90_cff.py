import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/70000/8068C0C6-CA9A-E711-A0C8-008CFAF0842A.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/70000/EEE0CDF6-D999-E711-A0CB-001E67E6965D.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/90003/DE976B88-5A93-E711-9E48-0025905C42A4.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/90001/0C557E79-6099-E711-BBF1-3417EBE64BB5.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/10000/36F9F519-6C93-E711-A4C3-0CC47A5FC491.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/90001/AAEDD6E4-E898-E711-B5EB-008CFAF73424.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/90001/1EF968BD-0399-E711-9531-D8D385AF8B64.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/90003/EA0E31BA-2099-E711-BE3A-1CB72C0A3DC5.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/90000/68AE95B5-2193-E711-AE46-E0071B73C610.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/90001/B49BCA90-B998-E711-B74E-C81F66C8BA4C.root',
       '/store/data/Run2016H/MET/AOD/07Aug17-v1/90001/02A46A47-4F92-E711-A118-C81F66B73FCE.root',
] )
