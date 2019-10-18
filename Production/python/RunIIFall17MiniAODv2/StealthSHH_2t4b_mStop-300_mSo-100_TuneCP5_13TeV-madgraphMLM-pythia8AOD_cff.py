import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A8F96C34-D499-E811-8B77-F8BC1234F308.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5CC7111A-9A9A-E811-96ED-549F3525BC38.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/0C46FF5C-359B-E811-8039-E0071B7B2320.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/48F0B00F-7999-E811-BFAD-00000086FE80.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/3877D02E-639A-E811-B63D-5065F38102F1.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8262AD0D-639A-E811-90E2-E0071B7AC710.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4254DCA8-969A-E811-8B84-EC0D9A89AA0A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/8CE18DD6-439B-E811-993D-3CFDFE6349A0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1AF235EF-439B-E811-A40B-3CFDFE634FA0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BE56D4E8-439B-E811-A650-3CFDFE639AE0.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/EA3E4BE5-439B-E811-BA4C-3CFDFE63F320.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B63CA4D6-439B-E811-B8E8-90B11C443471.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/2E54744D-CD9A-E811-B10A-FA163EDD3A25.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/109176AC-F79A-E811-A6D7-FA163E06E101.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A07ECA55-CD9A-E811-9B3F-FA163ECE80EF.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/826EEA9B-079C-E811-B96D-02163E017FB2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/24A3BF8C-109C-E811-9988-FA163EE4A297.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/6CAB1A0E-7D99-E811-A618-0CC47A57D036.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4A133DEE-929A-E811-B9CD-0CC47AA53D66.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A4998C4F-6799-E811-974D-0025905A60F2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/927FE7CA-A899-E811-88C8-0CC47A4C8E56.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E01B7CDD-A899-E811-A046-0CC47A4C8E3C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BC9696CB-A899-E811-9586-0CC47A745294.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/441F5BD8-A899-E811-AF3C-0CC47A4C8E2E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D8A81F1D-6999-E811-BF94-0025905A60E4.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5C12DDD1-6899-E811-ABC8-0025905A60E4.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/801B5A6A-FD99-E811-B8E9-0CC47A4C8E1E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/58EFFF7D-D499-E811-96F0-0CC47A4D762A.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/1E18FB1E-A999-E811-969F-0025905A609E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/887CEA7B-D499-E811-AC73-0CC47A4D7668.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/E2956094-6E99-E811-8C21-0025905A48B2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4A147FB1-D399-E811-8C57-0CC47A7452DA.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/7A8A68C8-D299-E811-8086-0CC47A7C357E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C01A0C32-A999-E811-AB4E-0025905A608C.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A64E78DC-D299-E811-BAB2-0025905B85A2.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/BAC8C75C-CF99-E811-98DA-0CC47A4C8F08.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/C0F0E4E2-0C9A-E811-ABED-0CC47A7C3432.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/564386A1-FB99-E811-AE93-0025905B85D6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/AEDCE333-839A-E811-8390-0025905A609E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/A48E9E1F-0C9B-E811-8105-EC0D9A0B3050.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F81E628E-729B-E811-8E56-0025905AA9CC.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/508315E7-9F9B-E811-8F6A-0CC47A78A3EE.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/5CC902B1-A59B-E811-A74B-0CC47A78A3EC.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/18CA3D00-A09B-E811-B4DD-0025905B857E.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/F641588F-A09B-E811-B43F-0CC47A7C35F4.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/D6F143BA-9F9B-E811-8F1A-0CC47A7C3430.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/749FBD05-079C-E811-8F18-0CC47A4C8EA8.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/4608641B-A29B-E811-A1F1-0025905A6138.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/B2C94E21-A29B-E811-906C-0025905A60CE.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/FC3494AF-A09B-E811-BD90-0025905A60A6.root',
'/store/mc/RunIIFall17DRPremix/StealthSHH_2t4b_mStop-300_mSo-100_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/PU2017_94X_mc2017_realistic_v11-v1/00000/64BD2FBA-A09B-E811-91FB-0025905A60D2.root',
] )



























