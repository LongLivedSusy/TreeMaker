import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/0493D59F-90A5-E811-A58A-A4BF0112BD94.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/C070423A-C2A5-E811-AFD4-A4BF0108B532.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/E6E8D0CF-AAA5-E811-9CDE-A4BF0112BD7E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/5634A9D8-90A5-E811-8804-A4BF01125698.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/86DA36AA-BAA5-E811-BEB3-A4BF0112DE3C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/926C1EA7-BAA5-E811-804C-A4BF011253F0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/AE079FB7-BDA5-E811-96A8-A4BF0108B232.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/4A037DBE-F5A5-E811-9DEC-A4BF0112BD7C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/BE5AC17D-90A5-E811-8C62-001E67E69DEC.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/B61A2414-BCA5-E811-BF55-A4BF01125810.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/80D11FFF-C2A5-E811-8E76-001E677925E6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/1E55ED83-BDA5-E811-8DFC-001E677928D2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/9A0E7ADA-C2A5-E811-B4B0-A4BF0112BC7A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/D0590F63-FBA5-E811-8941-A4BF0108B532.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/4E751CAA-C2A5-E811-B133-001E677926DA.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/92BC7D1D-0DA6-E811-8D4D-001E677925E6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/8C3F4914-D3A5-E811-8670-A4BF0112BD22.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/CC39BEAB-BEA5-E811-96AC-A4BF0112F52E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/4CE66487-EBA6-E811-9A9F-001E67792594.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/F438E2E6-57A4-E811-A74B-7845C4FB82F2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/661EF66C-20A4-E811-AB73-F04DA27541F0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/26790F53-51A4-E811-92A7-00266CF89604.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/4E788D60-85A4-E811-BC3D-5065F38122D1.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/86D91FAA-C5A3-E811-B6A7-A4BF0112BE0E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/B6658FEA-71A4-E811-B828-A4BF0112BC1A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/5ADAD934-7EA4-E811-B4F2-A4BF01125BA0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/E2A91A3D-56A4-E811-A0B6-002590796302.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/9473D37A-7FA4-E811-8CD9-A4BF0112F778.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/3A76493E-39A4-E811-BF7D-A4BF01158A50.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/1432D194-97A4-E811-8095-001E67CBE45A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/4053FA66-86A4-E811-97D8-A4BF011588E0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/D47711A2-E9A4-E811-8FE7-A4BF0112BDB6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/AA5131A2-50A5-E811-8643-A4BF0112BC7A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/3894701F-BBA3-E811-AB4A-842B2B688F18.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/142CDC9B-56AC-E811-A2D1-B49691091B34.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/AE474228-8CAB-E811-9439-E0071B7A7870.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/B2AD28AF-96AB-E811-8FD9-141877639F59.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/DC8225CC-F5AB-E811-8DC2-0CC47A4D7698.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/345713EB-0FA9-E811-829F-A0369FE2C21A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/E257A21B-10A9-E811-867E-066F320000B8.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/FC2C3FA0-56AC-E811-92B1-AC1F6B0DE2EC.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/506D3CAA-56AC-E811-9CF7-842B2B6F84A7.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/0621CE56-8CAB-E811-AAE2-0CC47AFB80DC.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/9843B3C5-8DAB-E811-9E97-0025905C53B0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-450_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/60DCAB23-95AB-E811-81BF-001E675827BC.root',
] )
































