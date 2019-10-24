import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/5458AB80-F2BD-E811-9F47-5065F3812221.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/728F3FB0-83BE-E811-8452-5065F38162B1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/B8ADC234-44BF-E811-BB11-24BE05C44BC1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/441FA45A-44BF-E811-8AA5-1C6A7A21B7CD.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/68FE339F-94BF-E811-85F7-008CFA1CB470.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/A0F9887B-94BF-E811-AC1D-90E2BAD57CD0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/BE96EEA5-94BF-E811-B9CC-001E675A6AA9.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/8CD93F1A-0BBE-E811-877C-1866DA85DD9C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/3E34B89B-94BF-E811-8536-246E96D14E34.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/545831A7-94BF-E811-AC97-008CFA007C18.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v2/100000/323B9E25-21BE-E811-91EC-001B219D5C26.root',
] )





























