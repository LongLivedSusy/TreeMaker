import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/F4704DC4-3EA6-E811-A191-A4BF0112BE1E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/CA1B8FA3-E7A6-E811-A9E8-A4BF011253A0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/10655943-20A7-E811-BAC7-001E67792514.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/94474684-F5A6-E811-A41D-A4BF0112BBDE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/726A1459-1FA7-E811-929B-001E67792680.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/26105C40-05A7-E811-996D-A4BF0112BCE0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/DC5EA9EE-04A7-E811-B29D-A4BF01125810.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/2A48D1B1-05A7-E811-B794-002590A83160.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/442D72A6-20A7-E811-8E7C-A4BF01125D56.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/6A1EF5D7-04A7-E811-BE58-001E677925A0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/7C6B7594-04A7-E811-B416-001E67E6F760.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/CC863DFD-99A7-E811-8BC5-001E677928A4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/3C3ED869-9DA7-E811-B5F8-A4BF01125810.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/4642AFFA-33A5-E811-B579-A4BF0112DFA0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/A82EFC1C-39A6-E811-8028-001E677928D2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/DEB38B5D-85A6-E811-8609-001E67792510.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/70CAAD4A-87AB-E811-8959-0025905C54DA.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/E4079D45-6AAA-E811-8C2E-A0369FD0B306.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/264D7C00-6CAA-E811-AB99-A0369FE2C152.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/6047AD57-59AB-E811-8A7C-F45214101150.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/D6A1E84C-17AB-E811-9DEF-FA163EAE6EF0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/98E53C05-19AB-E811-8D16-001E67DDC2CC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/AA551D48-87AB-E811-97F7-44A842CFC98B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/D09F5CC5-87AB-E811-8418-0CC47A1E0466.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/48CF856D-87AB-E811-BAEB-A0369F3102B6.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/80000/BAFB0EA0-1EAB-E811-B7A8-44A84225C8DB.root',
] )

