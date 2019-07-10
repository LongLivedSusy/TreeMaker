import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/6080E31A-9C95-E811-A2DD-B8CA3A70BAC8.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/289935D6-1C9A-E811-AF1E-0CC47A4C8ECA.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/8A8CF47D-639C-E811-9FFB-001E67E6920C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1E1210A8-639C-E811-989F-3CFDFE6399A0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/7C9FCAC1-E29E-E811-B766-B8CA3A70A520.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/38AB384B-A09F-E811-A04A-EC0D9A89AA0A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/60E1CE21-6E9D-E811-8A4D-0CC47A0AD6E0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/3C59E9A5-E6A5-E811-B8CA-008CFAFBE8F2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/307287DB-BEA1-E811-A923-EC0D9A8221E6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/162C3AD3-ACAA-E811-88CB-008CFAF747AA.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1A1D56FD-B1AB-E811-8608-509A4C858BCB.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/F0E4A882-84A9-E811-9CBD-44A842CF058B.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9039799D-9DAB-E811-A746-0CC47A4D765A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9AE2C3E7-84A9-E811-BCEB-5065F38162B1.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/5CA7AEB3-5DAC-E811-AB5A-FA163EB5B592.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/F4633954-9DAB-E811-B06F-90B11CBCFFB6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/86000497-9DAB-E811-A460-008CFAE4507C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/42D03043-9DAB-E811-89DE-842B2B6FE64A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/76C31B33-83C3-E811-AB0D-3417EBE644B9.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-550_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/342B541C-DCC3-E811-9E3A-7CD30ACE17F2.root',
] )














