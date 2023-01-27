import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70001/24808760-8686-E711-AC4F-0025905B85CA.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70002/44B7B001-0087-E711-B8B2-0CC47A6C1866.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70003/621577FA-6E87-E711-9AF0-001E67581494.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/110000/4CFAFE49-F285-E711-A93D-90B11C172CCA.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/110000/841390D7-4586-E711-8A0B-B083FECFF6AA.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70003/32F59125-1A87-E711-9EB1-0CC47A78A4BA.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70003/188C9A87-2887-E711-A22A-008CFA197438.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70003/22F926FA-2A87-E711-A731-008CFA111268.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/110000/5AAC4E8C-3186-E711-8CB2-002590FD5A78.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70003/92B57368-2A87-E711-85C9-FA163E86321F.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/110000/6EA73738-F285-E711-ADE9-5065F38122A1.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/110000/DE01BBD1-2886-E711-84D0-0CC47AD9908C.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/110000/F49E2107-1B86-E711-9E85-0CC47AACC8A0.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70003/EC6F095E-1287-E711-8AB6-484D7E8DF085.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70000/EE759FF4-1185-E711-AED4-00215E2EAD28.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70001/F21E2B6F-9986-E711-B143-0025905A48EC.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70002/C2D6C39D-C286-E711-927F-0025905A60EE.root',
       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70002/C0A6BB6A-B786-E711-BF75-0CC47AD98CF8.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/70002/AE3698A1-DF86-E711-B871-0242AC130002.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/50001/4A5A5509-6E87-E711-AFEF-0242AC130002.root',
#       '/store/data/Run2016H/SingleElectron/AOD/07Aug17-v1/110001/1A8B4C67-5586-E711-B4FC-002590FD5A48.root',
] )
