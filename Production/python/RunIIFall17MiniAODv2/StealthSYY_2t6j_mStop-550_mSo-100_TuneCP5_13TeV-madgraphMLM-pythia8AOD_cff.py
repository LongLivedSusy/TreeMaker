import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/26FF603A-7495-E811-B6B6-1866DA85D967.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BC343DA4-9198-E811-93C3-5065F3810301.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C82A6F16-6E98-E811-889C-EC0D9A82260E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/AAB34496-8D9A-E811-BEAB-44A842CFC9BF.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/947F92A9-C69A-E811-B635-C4346BC78A40.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D4BC644F-6999-E811-BA87-0CC47A4D75F8.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A6F944CC-CF99-E811-9488-0025905B8612.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/26B8FEF5-C59A-E811-97E5-AC1F6B0F3A26.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FE2B9890-099B-E811-8EF9-0CC47A2B04A6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0ACCE912-2B9A-E811-A7F6-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C4F6B7AE-9298-E811-9822-0CC47A4C8E34.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/EE5F2A6D-6999-E811-9DEF-0CC47A4D76AC.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FAC266EC-CF99-E811-93FD-0CC47A7C340C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D633154B-F899-E811-B0F8-0CC47A745298.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/44827D71-D099-E811-AB2F-0CC47A7C3612.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8ACD1730-F599-E811-8382-FA163ED71987.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/CA5192C8-EF9A-E811-8105-FA163EACCAC4.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/60FDF40C-C69A-E811-AD76-D4AE526A0488.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/410000/A81EBE11-68A8-E811-876B-24BE05CEADD1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/E08B5349-96A8-E811-A1D1-24BE05CEFB41.root',
] )











