import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A4D909DD-0998-E811-B196-FA163E8B4641.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2CFB9BC9-0998-E811-B88E-0090FAA575B0.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/047C2E9A-DA97-E811-8349-0242AC130002.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/94B96538-0A98-E811-BD2C-801844E561F8.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0872C9DA-0998-E811-8213-5065F38162B1.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/CC03DD3E-0A98-E811-8923-141877635B57.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4E073CFD-7197-E811-8728-0025902D944E.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/ECDF1C2B-0A98-E811-B0F5-008CFA110C60.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/DA8C7678-7397-E811-B630-002590DE6E2A.root',
'/store/mc/RunIIFall17DRPremix/StealthSYY_2t6j_mStop-900_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/30000/E0178973-249D-E811-AE7E-00259075D72C.root',
] )










