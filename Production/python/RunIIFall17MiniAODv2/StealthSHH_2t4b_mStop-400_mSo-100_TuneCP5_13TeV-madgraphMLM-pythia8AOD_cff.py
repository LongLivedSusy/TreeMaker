import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1442EC81-7FA4-E811-A173-24BE05C3CBE1.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/868840AD-46A5-E811-9E3F-FA163ED7F85C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A00938F8-4FA5-E811-9F97-FA163EDC2934.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/10D9C529-56A5-E811-B3BD-FA163E8211F9.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9812D9AA-14A5-E811-A556-FA163E2A6957.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/DAD55D25-D2A6-E811-A6BD-FA163EA1368E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/6CA872C6-43A7-E811-84BA-FA163E8BA02A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/3AB2C6B9-3DA7-E811-AA10-FA163E7CAD4F.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/D2079985-66A7-E811-AE83-FA163EA5D5A9.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/20581C9F-66A8-E811-AD35-FA163E3593E9.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/B6114BA8-66A8-E811-AE50-FA163EDB013A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/784A3799-66A8-E811-AE05-FA163E120D15.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C4B946A1-66A8-E811-BB63-FA163E038E39.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A8442DA1-66A8-E811-80CF-FA163EFA689B.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A01817B4-66A8-E811-B532-FA163E4BB802.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/F89F3CB4-66A8-E811-BF79-FA163EB84E0D.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/80D4C9B5-66A8-E811-9C87-FA163EE66323.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/FC67C69F-66A8-E811-A644-FA163EC861A6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C841A9A8-66A8-E811-A2C0-FA163E7E1149.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/AAB358B9-66A8-E811-835B-FA163E81C56B.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/F4A6BAA1-66A8-E811-9185-FA163E3D538E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/E44541BE-66A8-E811-BC8D-FA163EED90F7.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A07FE4A2-66A8-E811-BA71-FA163E6FB017.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/D43200AF-66A8-E811-A39D-FA163E104BF4.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A84C46B2-66A8-E811-B464-FA163E55CE78.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/DA3617A7-66A8-E811-8FB0-FA163EB4138A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/42C9BCB1-66A8-E811-AEE5-FA163E050166.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/18D741AD-66A8-E811-84E7-FA163EA392AD.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/F4984DB3-66A8-E811-AB5B-FA163E7DE5C1.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1A3667B3-66A8-E811-9562-FA163E891257.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/863675C0-66A8-E811-812F-FA163EDC6DF2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/8495FCB3-66A8-E811-822E-FA163E21EF7F.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/720B70BE-66A8-E811-ACA5-FA163E75C6E8.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9C5F4ABB-66A8-E811-8ABC-FA163EE4A297.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/C6B982BD-66A8-E811-98DC-FA163E2DA488.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/22A891B9-66A8-E811-AB33-FA163E11B3E0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/08B0B8B8-66A8-E811-AB88-FA163E54ACA9.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/2A66F7DD-66A8-E811-8FE5-FA163EE59243.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/8AD0E1BA-66A8-E811-9659-FA163ECA8E83.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A6125101-67A8-E811-A6CD-FA163EB43663.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/52A1FBBC-66A8-E811-BAB9-FA163EB02DCD.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/427A12B0-66A8-E811-A4FC-FA163EB8F22B.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/12632FD0-66A8-E811-AAAE-FA163E1B57DB.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-400_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/AC66B2D2-66A8-E811-ABF3-FA163E14A82F.root',
] )






















