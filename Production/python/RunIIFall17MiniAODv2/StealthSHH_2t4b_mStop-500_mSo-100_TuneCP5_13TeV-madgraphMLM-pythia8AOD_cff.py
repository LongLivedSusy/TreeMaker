import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2A76B1E3-6B9C-E811-8B0F-0025904C66F4.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/DE98B730-879D-E811-AF2D-A0369F83633E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6886A341-2E9B-E811-A13D-A4BF010F0F08.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/EED9E39C-5E9B-E811-97A4-002590A887F2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/1C67C45E-B99C-E811-89E1-A4BF0112BD4E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/22B8D5F5-BE9C-E811-A445-A4BF0112BCE0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A26BB43D-449A-E811-97D7-008CFA1113A8.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/30B778A1-E19B-E811-809C-008CFA197B74.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/000E0541-4199-E811-8D4C-D067E5F914D3.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6E83DC59-449A-E811-8F30-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/EE0C383B-879D-E811-91F7-F04DA27541CF.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/B25E09C4-F59B-E811-A809-0CC47AD98B94.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/D8B1FB92-5D9A-E811-9F59-002590D9D880.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/48A6CAA2-F59B-E811-9514-24BE05BDBE61.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/3C0CC916-8D9C-E811-9A19-24BE05C3DB21.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/369903BD-6B9C-E811-AE1B-5065F3818291.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/66297BF3-F79C-E811-B6DC-EC0D9A82260E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/0A7A0936-879D-E811-B20B-001E67580BAC.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F4F4F0C7-F59B-E811-A82A-008CFAE4520C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/6CA865E1-729C-E811-B34B-0017A4771078.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/60EEE5B5-5B9D-E811-926A-20474791CCC4.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/28B08503-869C-E811-B1F8-0CC47A7EEC70.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2467F92F-989B-E811-9932-0CC47A7C3422.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/F0D654BF-349C-E811-A2B6-141877411EA2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/A4A1E371-879D-E811-A92F-D4AE527F4A7B.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/80257733-879D-E811-BFC0-0CC47A4DEE2A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-500_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/10000/3A74D269-67A0-E811-BA34-001E67A39C17.root',
] )













