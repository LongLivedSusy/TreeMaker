import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/CAF13C32-C19C-E811-A107-A4BF0112BC2A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5AFCF20A-349C-E811-853F-0CC47A4DEF3A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/BE546B3A-349C-E811-A566-008CFAED6E60.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/22E91E75-349C-E811-8B8E-1CB72C1B6CCA.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/7E77CFFD-339C-E811-B39E-5065F37D2172.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/CCCCF42A-349C-E811-9FD9-00A0D1EE928C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/5894D410-349C-E811-AABF-D4AE52E7F60F.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/800D792F-349C-E811-B223-00266CF94C00.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/9C953F52-2F9B-E811-B90D-0CC47ADAF60A.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-850_mN1-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/C89F304A-F19B-E811-88CA-0242AC1C0501.root',
] )





