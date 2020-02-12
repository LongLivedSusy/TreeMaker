import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/FAB907A3-7DC0-E811-B7C8-24BE05CE1E31.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/E05E13DF-7DC0-E811-B72F-24BE05C49891.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/2816048D-CACB-E811-913F-0CC47AD98D08.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/6E6D2401-66CC-E811-A11A-A0369FD0B10E.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/D0E016B2-79CC-E811-A7E4-B8CA3A709028.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/7C614BED-69CC-E811-807F-0023AEEEB6FA.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/1A1CFB44-C9CB-E811-BE02-0CC47AFC3C72.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/C4AA2E61-BED0-E811-B8C1-008CFA197DF8.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/343C428E-D1D0-E811-9313-008CFA197480.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/A60CBE59-D9D0-E811-B770-008CFA197CA4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/62447DB7-A0D0-E811-A6FD-008CFA197480.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/A27CD83D-A1D0-E811-89CB-008CFA1979BC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/124E26B9-A0D0-E811-B550-008CFA11118C.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/5EA621B5-A0D0-E811-A92E-008CFA0646CC.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/621884B9-A0D0-E811-AF1B-008CFA197AA0.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/146F8BB8-A0D0-E811-B1D8-008CFA111184.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/8EBE10B0-A0D0-E811-BE88-008CFA111220.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/4E30A9BD-A0D0-E811-9399-008CFA14F970.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/B4AA7499-A0D0-E811-B53A-008CFA197C68.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/10B54FDA-E6D0-E811-AD4E-008CFA197D14.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/2000C1C8-A3D1-E811-ACFF-008CFA1113E4.root',
'/store/mc/RunIIFall17DRPremix/RPV_2t6j_mStop-500_mN1-100_TuneCP2_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/110000/96E6583E-39D2-E811-BDE4-008CFA165F34.root',
] )




































