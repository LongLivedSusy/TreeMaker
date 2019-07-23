import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/5E878B31-31C4-E811-BDE9-EC0D9A8222F6.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/7C015523-33C4-E811-93EF-EC0D9A8221FE.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/9266442A-F1D0-E811-AB00-FA163EDDC661.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/6274CF48-F1D0-E811-BC2E-0025905B85CA.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/08333A38-F1D0-E811-A96D-48FD8E2824AD.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/982C9486-F1D0-E811-A302-20CF300E9EC8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/8EB0994D-F1D0-E811-BD02-00266CFE8A04.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/528F0CC4-AAD1-E811-BF7B-44A842BE8F8B.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/569AEABD-AAD1-E811-BA08-0023AEEEB208.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-600_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/60000/70711F33-C8D2-E811-AAC0-0242AC1C0503.root',
] )



















