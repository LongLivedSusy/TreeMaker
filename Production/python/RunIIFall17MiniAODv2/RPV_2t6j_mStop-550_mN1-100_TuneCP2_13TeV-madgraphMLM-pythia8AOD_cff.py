import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/D204D09C-03BF-E811-B81A-A4BF0102611B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/ACCE8167-01BF-E811-8684-A4BF01013F29.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/D0FAD2ED-2EBF-E811-B0D5-EC0D9A0B33A0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/3C58C968-07C0-E811-AE2E-0026181D2917.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/F6205CFC-D6BF-E811-99C2-0CC47A7C353E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/16B593D6-B0C0-E811-8276-0025905A6076.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/DEB5F234-7CBF-E811-9EFF-0CC47A2AED0E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/1C7EC6B5-5CC0-E811-A8FA-002590E3A286.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/F2CE4CA4-7AC0-E811-9E82-003048F5B69C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/78984485-7AC0-E811-87B5-002590E2DDC8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/F2272BED-4DC7-E811-ABEE-001E67A3EBD8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/3C37CD0E-90C7-E811-9B48-24BE05C656A1.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/060DE6A5-A0D0-E811-889A-008CFA1112A0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/DA9A05B6-A0D0-E811-B395-008CFA165F40.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-550_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/688AD036-3AD2-E811-AEF1-008CFA197D34.root',
] )


