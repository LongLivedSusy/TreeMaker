import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/7670D54C-5DD4-E611-8860-0CC47A57CBCC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/AED31466-18D5-E611-9A38-002590D9D968.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F691B265-B1D4-E611-93D9-00259073E4A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/2EA39EA4-B5D4-E611-A191-0090FAA56F60.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6857EFB1-14D4-E611-98EB-1866DAEB3628.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/B49AE20C-64D4-E611-AE94-141877411D83.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/70612547-18D5-E611-97C1-C81F66B7C6E1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/5AD6E851-18D5-E611-B0FB-001E677925E2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3EC7AECC-F9D3-E611-943D-C81F66B7EAE5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/82A5734C-FCD3-E611-9A1B-549F3525B9A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/24F98400-28D4-E611-A5EA-B083FED40671.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6263F07C-FCD3-E611-8067-44A84225C893.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/686F6FFC-FFD3-E611-A831-44A84225CABC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/106C9BA8-28D4-E611-8F13-14187764278D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8650D84D-18D5-E611-B447-ECF4BBE16148.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/4886955C-18D5-E611-919C-02163E01767C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A2B15DFB-59D4-E611-95CD-002590E7DE20.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/184EEDD1-6DD4-E611-B2CF-002590E7DFA2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/448E0810-71D4-E611-B4F2-002590E7DFFE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6A64F41C-77D4-E611-B369-002590E7DFFE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/B4DD6D5E-7BD4-E611-B226-002590E7DE24.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/74F3D491-88D4-E611-B373-0CC47A1E046E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/7E14F440-8FD4-E611-848B-002590E7D7D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/AEEF0B34-92D4-E611-8512-002590E7DF2A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8CBA2EB7-93D4-E611-AB1B-0CC47A1E0DC2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/00A3CE55-99D4-E611-9B30-002590E7DFE4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/86599B68-9BD4-E611-98B7-002590E7DFEE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/82555BE1-97D4-E611-882D-0CC47A1E089C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/985E4A7B-9FD4-E611-9A01-0CC47A1E0C76.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/426E68F4-A3D4-E611-80B5-002590E7E00A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/B888D36A-18D5-E611-A909-0CC47A1E0DCE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/BA496F61-1ED4-E611-88D2-FA163EC2B95D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/CE14B105-18D4-E611-9D7D-0CC47A044888.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A075DE36-18D4-E611-9FDC-02163E00B2D9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D44743E9-59D4-E611-8F12-FA163E37973C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/FAD428FD-57D4-E611-AA9B-FA163E0546A6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0E6A65ED-59D4-E611-B7E8-02163E00F69F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/44103AC5-58D4-E611-BD29-001E67C7AC24.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6A0B0704-5ED4-E611-A79A-FA163EE9CA73.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/2EFFF067-67D4-E611-AD78-02163E016120.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0E890164-18D5-E611-A693-FA163EF00B82.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/76232629-CDD4-E611-8249-0CC47A4D769A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/722EA618-CFD4-E611-BAC4-0CC47A4D76AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/04DDB711-CFD4-E611-A5A5-0CC47A4D7618.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/82BB162E-CFD4-E611-8737-0025905A60F2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/4E50685A-18D5-E611-8D2C-0025905A60D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D249C15B-18D5-E611-AB1F-0025905B8560.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/7ACA45E3-57D4-E611-916C-001E67A3F49D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/C27D9FFA-59D4-E611-9AB3-001E67DDC24A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/ECB05164-59D4-E611-B21A-D4AE529D9537.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/5E46D220-6FD4-E611-8D01-001E67A3F92F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/924758DA-72D4-E611-8EFF-90B11C05054D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D8C9313A-17D4-E611-A781-0CC47AD98BC2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/58E9A411-55D4-E611-AE5C-002590EFF972.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A8BB4FE2-57D4-E611-A711-0CC47AD98D06.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8410E4F3-58D4-E611-B691-0CC47AA992AE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/C4B12F62-59D4-E611-AF61-0CC47A13CB18.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/46476497-5AD4-E611-8D7B-0CC47A13CB62.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/1C355C82-5ED4-E611-ADB5-0CC47AD98B98.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/4290384C-18D5-E611-B5A3-0CC47AD98D0E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C240E039-FED3-E611-9D52-008CFA111310.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D8C28DF2-27D4-E611-8903-008CFA197B74.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/EE5E0422-CFD4-E611-884B-001E675813C4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F03EC468-18D5-E611-94EA-001EC9ADD6D2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/72FF33ED-00D4-E611-B991-0CC47A1DF7F2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D8F8E037-1DD4-E611-BD54-44A842240F8D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D25128FA-56D4-E611-9E09-002590D6013C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F20663FB-59D4-E611-93A8-00259073E36C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/DAB13E2D-5FD4-E611-8C85-002590D600E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/48119A9C-5DD4-E611-B0F6-20CF3027A5A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/9E89A8BA-62D4-E611-83DE-002590D600E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/7AB84165-64D4-E611-9279-20CF307C9944.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/EE674F71-6DD4-E611-9341-D4856459C3E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/4C55E868-6ED4-E611-944E-D48564593F64.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/CA94AA20-6ED4-E611-B714-20CF30725200.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/BA505D63-77D4-E611-B9FB-20CF305B053D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/20D6D8D6-74D4-E611-8921-D48564599C64.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/54C51C2D-7BD4-E611-94C9-44A84224053C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/9E2B7948-8AD4-E611-9E4B-141877636851.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/1A8043A9-8ED4-E611-B320-141877636851.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/4C753C38-8FD4-E611-B74C-20CF3027A582.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/063410CB-18D5-E611-98F9-002590D8C7E2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/3E99E058-18D5-E611-8CAC-0025904FE658.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1C446798-01D4-E611-8F6B-002590D9D8B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/74921FDC-27D4-E611-9F65-0CC47A0AD6F8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3ADC32FE-F6D3-E611-8555-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4A8D8AAD-F7D3-E611-BED0-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/46F404A6-F9D3-E611-8108-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A40BC983-28D4-E611-AB69-5065F3817281.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/FAF68663-12D4-E611-9AD7-E0071B7A5540.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/E83CDEC2-18D4-E611-A31A-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/E0CA4C44-52D4-E611-8368-B8CA3A70BAC8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A6598D6E-56D4-E611-ACB2-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6C92B6FC-59D4-E611-BB5B-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A835ED10-5DD4-E611-9627-24BE05C4D801.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A84FC207-59D4-E611-9640-008CFA197C34.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/C64926DE-5BD4-E611-A788-008CFA110C78.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D0DF414E-5DD4-E611-8D96-008CFA110AA8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0CF98D9D-62D4-E611-9ADE-008CFA1111EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/ECA000E2-64D4-E611-8DF1-008CFA110C78.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A45B2677-18D5-E611-8E87-008CFA1974DC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/5C0D0FEF-58D4-E611-A00F-B8CA3A70A410.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/28705290-5ED4-E611-A78E-5065F382F2B1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/C6DE0F7B-5ED4-E611-8868-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/7420ECB3-68D4-E611-B8DD-24BE05CECBD1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/3A80CC57-18D5-E611-8719-24BE05C3CBE1.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/70C87F1A-F8D3-E611-8EE4-90B11C2AB44B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CAB6A6AE-F9D3-E611-A797-0CC47AA99438.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EAE1B5AC-FBD3-E611-982F-0CC47AD98F70.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/70688E4E-FCD3-E611-B1F8-0CC47AD98B8E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/26C34ED4-27D4-E611-A48C-0CC47AD98BCC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BA6D46B6-05D4-E611-BE8C-0025904B0FC0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5E90B54E-28D4-E611-B3E7-0025904B2016.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CA1CB9BC-2CD4-E611-96EE-02163E0176D4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/00E5A7CE-FBD3-E611-802F-001E67E5A39A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4857C1B0-FFD3-E611-A457-A4BF0101DE18.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-250_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/42AD4DD4-27D4-E611-9331-A4BF010255AE.root',
] )





























