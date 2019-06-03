import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2C20DCD3-03BB-E811-A71F-A0369FC5EE94.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FEA8D3DE-50BB-E811-B657-002590D9DA9C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/52B81D0B-04BB-E811-8491-7CD30ABD278A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/12EC0A79-50BB-E811-A04F-20CF3027A55F.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/623B51A2-50BB-E811-B459-24BE05C626B1.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C67F73CD-50BB-E811-A564-0CC47A2AECFA.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/042D2B20-51BB-E811-A5CF-0242AC1C0500.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/001E7479-03BB-E811-A4BE-A0369FE2C152.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/620C0B86-50BB-E811-A58B-0CC47ABB518A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8EFBF2B1-03BB-E811-A53A-0025904C6216.root',
'/store/mc/RunIIFall17DRPremix/SMS-T1tttt_mGluino-2000_mLSP-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/3E325EE0-AEC6-E811-A45C-001E67DDD348.root',
] )


