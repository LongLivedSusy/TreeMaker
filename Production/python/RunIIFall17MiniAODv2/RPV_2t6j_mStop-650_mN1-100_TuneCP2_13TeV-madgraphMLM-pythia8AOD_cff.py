import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/CE994BF0-DEBF-E811-9021-A4BF0126D1BB.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/B27D4239-CCC0-E811-A349-A4BF0102A5F9.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/2C496EE3-64CB-E811-B945-48FD8EE73A79.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/84F573C3-AAC8-E811-B840-0CC47A5FC281.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/DC79B2FD-28C8-E811-B155-BC305B390A73.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/ACF3C000-A1C7-E811-8704-0CC47AA992B2.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/90A3155E-0AC8-E811-871E-E0071B6C9DC0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-650_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/100000/D64F5F64-E7D0-E811-9F4B-008CFA197DF0.root',
] )








