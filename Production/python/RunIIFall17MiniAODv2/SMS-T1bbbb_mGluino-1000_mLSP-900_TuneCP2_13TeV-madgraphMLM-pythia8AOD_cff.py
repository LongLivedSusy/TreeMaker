import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/A01DB610-30BB-E811-8DC6-0242AC1C0501.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/F0299488-2DBB-E811-BD0A-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/F8F8BF46-90BA-E811-AD60-0025905D1E00.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/4A57914B-73BA-E811-A6C4-0025905C2CBA.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/3E7CC033-6BBA-E811-9617-0025905C53D2.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/921B27EB-2BBB-E811-8110-0025905C3D40.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/60A3CDD3-32BB-E811-9169-A4BF011256C0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/02DF5D07-DCBB-E811-A9BC-A4BADB22B39D.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/50C17B3F-98BA-E811-A45F-F02FA768CB3C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/00404C55-60BA-E811-88A9-0090FAA583F4.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/282612A4-74BA-E811-AB94-203DB23FCC42.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/281A911B-99BA-E811-90AF-48FD8EE739EB.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/922F93B6-81BA-E811-9CAC-0601EA000261.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/F673215B-60BA-E811-A1D8-F02FA768CCD8.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/CEC61EF8-2BBB-E811-A989-A0369FD0B364.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/C8B39F1B-6EBB-E811-8501-346AC29F11B8.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1bbbb_mGluino-1000_mLSP-900_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/270000/8A777D1D-F4BB-E811-8B50-3417EBE2F2F5.root',
] )









