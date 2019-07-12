import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/90000/FA8B01DF-1FA8-E811-98BC-A0369F30FFD2.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/90000/C2DC2D82-1EA8-E811-9D33-E4115BE5F180.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/90000/A8C87002-E9A7-E811-95DC-00259048AC10.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/60000/48946763-2FC6-E811-8A4D-0025905C2CBE.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/270000/3E6191AF-B9C6-E811-B663-20CF300E9EDD.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/60000/8C266347-0AC7-E811-BFB0-0090FAA57690.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/60000/10996117-37C6-E811-BCF1-008CFAFC03F8.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/60000/6E59F4F6-09C7-E811-A5B6-D48564599C64.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/60000/4E4416EF-0BC7-E811-93EC-AC1F6B1B23C6.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/60000/1AB1AABD-2FC6-E811-98EF-5065F381C1D1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/60000/F84740B3-2FC6-E811-8E73-A4BF0112DC2C.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-700_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v3/60000/CC6C3B70-2EC6-E811-8AC0-002590E2F664.root',
] )
















