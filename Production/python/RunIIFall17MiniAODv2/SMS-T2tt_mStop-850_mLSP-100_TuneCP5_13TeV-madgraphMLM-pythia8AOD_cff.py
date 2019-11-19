import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/3ED81B8C-E36E-E811-9ADA-001E675A6928.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/328163B0-486F-E811-AF2F-002590E7DE70.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/28D78663-7B6F-E811-A636-F4E9D4A36760.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/4839C993-2B70-E811-83C1-001E677926A2.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/0EF60A72-7E70-E811-97A0-7CD30AD09DC0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/1C4EB24F-A770-E811-B6DC-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/3ACFAAF4-6B6F-E811-AB06-0CC47AA992B4.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/567B683D-D46F-E811-A747-002590E39D8A.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/9CEC98DA-FE6F-E811-AAC9-509A4C83EF12.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/A20FE8FD-3D72-E811-8EB8-A4BF01125AD0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/D073AC17-0973-E811-B13B-1418774108DF.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/241F384B-CA70-E811-B076-90E2BAC9B7A8.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/3860BD5D-6E71-E811-8AB4-90E2BAD1C730.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/24493DE9-2773-E811-B711-A0369F83641E.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/102E1485-3A72-E811-BF1E-7CD30ABD2EE8.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/885C3F1A-3D72-E811-81D3-44A842BECCBE.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/4EFEADCA-027B-E811-8387-C4346BC00270.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/2028AD33-277A-E811-BA65-FA163E161C1D.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/20000/0A01DB33-277A-E811-B022-FA163E7A194F.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/020000/064A3BF4-588D-E811-B41E-7CD30AD09DC0.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F6860B78-7D8D-E811-87EB-509A4C84543E.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/020000/127DC357-5B8D-E811-BA4A-509A4C8339E9.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/020000/A8FCB346-588C-E811-AE6F-509A4C7489AF.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/020000/6E2CB513-588C-E811-BABE-509A4C730E32.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1C2EA92E-348D-E811-A6F7-7CD30AD08ED2.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/205EFD17-E68C-E811-8742-A0369F83630C.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4E32EED0-E98C-E811-9A36-00266CFF0ACC.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/210000/30C3ABB1-F079-E811-A730-7CD30AD0A696.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/766783E4-7073-E811-A4F0-001E67DDC4AC.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/2E1F19A3-1574-E811-B830-D4AE5264CC82.root',
'/store/mc/RunIIFall17DRPremix/SMS-T2tt_mStop-850_mLSP-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/50000/682695EC-3872-E811-9122-0CC47A7FC702.root',
] )

































