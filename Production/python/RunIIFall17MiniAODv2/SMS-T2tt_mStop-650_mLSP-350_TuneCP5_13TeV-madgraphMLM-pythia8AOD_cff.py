import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/8CDED5E3-8A70-E811-A8D6-5065F381D212.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/04C2E165-7470-E811-B666-0CC47AA9943A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/567DC903-B970-E811-9E29-1866DAEB5C74.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/7066F251-7873-E811-A527-5065F381F291.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/48429BA2-A471-E811-A2C0-008CFA165F34.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/845D7F31-A871-E811-B053-008CFA197954.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/F081B6A7-5973-E811-8A0B-008CFA16615C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/36DE3A86-5973-E811-95A1-008CFA165FE4.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/68B8E4F5-7973-E811-BC1C-0025905C431A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/666A461E-5973-E811-BAA3-FA163EB85918.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-650_mLSP-350_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/B8ED873F-DA73-E811-AD25-001E67792496.root',
] )












