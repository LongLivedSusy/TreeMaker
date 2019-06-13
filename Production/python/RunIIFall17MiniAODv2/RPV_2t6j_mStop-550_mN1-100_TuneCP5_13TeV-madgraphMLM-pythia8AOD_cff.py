import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/7CFE131A-C6AB-E811-AE25-002590A8882A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/F8E468F1-04A7-E811-BD09-A4BF01125550.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/9C8A253B-05A7-E811-8DAB-001E6779262C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/26F68581-5EA7-E811-A711-A4BF01125B18.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/ECF7A014-57A7-E811-9CE3-A4BF0115A278.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/C46DC46D-73A7-E811-A144-A4BF0108B732.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/1C5E017F-2DA7-E811-BC65-001E67E6F805.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/0A94496F-76A7-E811-8423-A4BF01125358.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/C8952EDB-C5AB-E811-8610-F02FA768CF34.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/CC681558-3AAC-E811-9870-F4E9D4BC8B50.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/80BE6409-3AAC-E811-A7D2-141877638F39.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/DAF9A144-C8AB-E811-8AEF-0025905C3E38.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/423A5D6C-C4AB-E811-AFE6-E0071B7A7870.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/36D543FC-C3AB-E811-847F-D4AE5290244F.root',
] )




