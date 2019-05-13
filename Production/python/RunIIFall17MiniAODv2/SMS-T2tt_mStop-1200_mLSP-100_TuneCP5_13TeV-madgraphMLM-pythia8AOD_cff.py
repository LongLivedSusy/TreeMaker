import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiless = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiless)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/6A562220-806F-E811-9572-008CFA1C9308.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/D6F3566A-846F-E811-9137-1866DAEECFDC.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/3E88BCA2-DA6F-E811-9548-1866DAEA8218.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/CE9C611A-E670-E811-B03F-842B2B0A39C6.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/18961AFF-4B70-E811-82D8-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/D88AB6C8-246E-E811-BB5A-5065F37DC4B2.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/D0BFD109-F271-E811-9AD2-90B11C2AAEEC.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/5241F97A-F171-E811-A87F-0CC47AA98A3A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/126E802D-6172-E811-BF38-1C6A7A26E149.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/5A46D70B-6172-E811-B0AD-1C6A7A26E149.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/1EE2F4CA-B270-E811-BCD2-001E67D89532.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/B02D06E5-A475-E811-B4B3-FA163E23C88C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/12402221-1476-E811-915C-008CFA197CA0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/EAD70D9C-A275-E811-8173-24BE05CEFB41.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/9631A0DE-A475-E811-B4CC-001E67792422.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/2A4CB2F9-1376-E811-96A2-0CC47A4C8F06.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/8217892B-1576-E811-B26E-3417EBE34A8F.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/210000/56C17684-BB79-E811-A694-14187751BEA0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/210000/8613344E-FD79-E811-9131-44A8423524BC.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/4E608519-5D7A-E811-9593-0CC47A4D7616.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/26C83CD2-5C7A-E811-8863-0CC47A78A418.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/46B0EA13-BA7A-E811-92E0-0CC47A4C8EB6.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B438DB86-BA7A-E811-8897-0CC47A4C8F26.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/00C09C59-F37A-E811-9159-0CC47A4C8E56.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-1200_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/FE1F5AC0-F37A-E811-B883-0CC47A4C8E22.root',
] )
