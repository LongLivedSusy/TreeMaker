import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/704CABF6-76A9-E811-A1AF-842B2B6F5F37.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6AE05489-F7A9-E811-B232-FA163E811509.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C6EA3590-13A9-E811-9D8F-0CC47ADAF60A.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5C8B430A-2DA9-E811-9120-0CC47AD98F78.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0CB02D18-3DA9-E811-BBE6-0CC47AD98D26.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7AB5E252-06AA-E811-BF1E-0025901D08E8.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/26953CFD-12A9-E811-A899-00000086FE80.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A8271DA9-3AA9-E811-A088-5065F38102F1.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B6D5400F-63A9-E811-87BF-00000086FE80.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A00B51A8-7FAA-E811-B25C-24BE05C4D851.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3852570C-ABA9-E811-AEAD-0CC47A57CD56.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/00432215-0FAA-E811-8AFD-0CC47A4D7616.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5AB19645-4BAB-E811-92BB-0242AC1C0501.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9683C81B-ADAB-E811-B422-FA163E9C50B2.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/543C9E4F-6AAA-E811-8BFD-484D7E8DF0FA.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D09BBE26-6AAA-E811-8C64-001E67D80528.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AE59CD64-7CAA-E811-8C86-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/963F9126-0FAB-E811-B640-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/46BDDC83-C9AB-E811-85AC-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/663765D8-7BAA-E811-B00F-246E96D14B5C.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FA027D14-0EAB-E811-B4A3-EC0D9A847EAA.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DE5F765C-0EAB-E811-81B5-E0071B7AC770.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/76BF822D-C5AB-E811-9259-24BE05C676A2.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EEB76A34-16AB-E811-BF29-0CC47AA98B8E.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2CD4233B-C9AB-E811-8B0F-0CC47A13D418.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8460E213-3EAC-E811-A74A-0025905C53D0.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/988047A8-47AC-E811-A1B2-0025905C96A6.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7A1DCB39-59AC-E811-9E83-0CC47AFB81B4.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7E93691F-65AC-E811-A338-0025904C51FE.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5AD2F7D5-31AD-E811-99FB-0CC47AF9B13A.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DE06B9B7-D8AA-E811-8E92-001E67E6F8D7.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B6252486-94AA-E811-9CD2-90B11CBCFFD0.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7621717A-A6AA-E811-98F6-90B11CBCFF41.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4287BCE7-BAAB-E811-81AF-842B2B6F827A.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/203C5D5D-7BAB-E811-B336-0CC47A4DEE86.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A4384151-4AAC-E811-81A2-A0369FE2C00A.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4CE1A0EC-B3AB-E811-87B5-00266CFFA240.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/440A2A97-96B0-E811-8C59-0CC47AFC3CA6.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7A19688C-96B0-E811-A72D-141877642F9D.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EE347892-96B0-E811-AFEC-002481CFB40E.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BA4091A1-96B0-E811-AD36-008CFA110C60.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C62D4572-96B0-E811-A7B3-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/203E37A2-96B0-E811-9A64-EC0D9A0B3080.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AA1DB9A2-96B0-E811-8E0B-0CC47AD98D08.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C0810EAB-96B0-E811-BEAF-0CC47A0AD630.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A4B465A1-96B0-E811-8BB8-C45444922BD1.root',
'/store/mc/RunIISummer16DR80Premix/RPV_2t6j_mStop-500_mN1-100_TuneCUEP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B67B93A9-96B0-E811-820D-44A8424A1D64.root',
] )



