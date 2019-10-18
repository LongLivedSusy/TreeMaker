import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/8631D0A7-379A-E811-A279-008CFAE4526C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/74C4923F-7D9C-E811-84AC-0025905A60C6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B648324F-E09B-E811-B17E-1866DAEA8394.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/54721C75-E09B-E811-B345-3CFDFE634C80.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/3EF38DC3-7C98-E811-8749-EC0D9A82220E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B07FC3F8-299B-E811-9C09-A4BF0115947C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/3EBB144F-099B-E811-8A74-A4BF0112BDF2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/3E94836F-6E9B-E811-8FC1-001E67792740.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D4DD0925-899C-E811-977A-A4BF0112BBF8.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/14CF6C8A-D09C-E811-94D6-002481CFE80A.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AE4C1EB0-F399-E811-86E1-24BE05C618F1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2442D748-B29B-E811-87B8-24BE05C4C891.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2634BB07-C19B-E811-805C-5065F381D2C1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5C1E7ECB-B09B-E811-B8E3-24BE05CEED91.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/4C6839CF-499B-E811-99DC-28924A38DC1E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B4F4CB81-2E9B-E811-A510-BC305B390A73.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BCEE5952-F09B-E811-9ED4-0026B92779F1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F69E7F89-D09C-E811-AC25-BC305B390A4C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6E3371CE-5D9A-E811-A7C2-0CC47AA989C0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/62F48763-2E9B-E811-A810-002590E39D52.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/0637E337-D09C-E811-B6C6-001E67DFF735.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5E8E26AA-4A9A-E811-8DB8-0025905B8612.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/08667074-D09C-E811-98D1-0242AC1C0504.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5A3B7A8D-2198-E811-AC26-14187741212B.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7E8EF663-D09C-E811-9752-00266CFFC76C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/34FDC121-AA9C-E811-AF74-24BE05C33C61.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/AACBFF49-FB9B-E811-B4A2-0CC47AFB7D90.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/D097A3E7-ECA8-E811-B357-0CC47A4D7698.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/40000/F082188F-1FA9-E811-82B6-001E675A6928.root',
] )



























