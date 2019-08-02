import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/DA036EBE-F399-E811-A135-008CFAC94240.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B0E3DB2B-F098-E811-9EB4-24BE05CE5D21.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5C259EC6-1A9C-E811-8FA8-0023AEEEB703.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/008466BF-B09C-E811-A0BF-A4BF0112BE3C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/9AB50CBD-199C-E811-8EEC-24BE05C63791.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A621B96B-239C-E811-9B42-0CC47A5FA211.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8C967F7E-269C-E811-B9C2-02163E01A05B.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B246A4D0-1A9C-E811-93B2-0CC47A0093EC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/82FD6E07-1A9C-E811-B62D-0025905D1CB4.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6415DC48-169D-E811-AB47-20CF300E9EC1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C0891735-1F9C-E811-BD66-C4346BC75558.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/0465803D-1B9C-E811-B541-A0369FD0B2D0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/641BCB71-169D-E811-9EC1-001E67A3EA7A.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-600_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/22440155-169D-E811-B06B-141877411367.root',
] )





















