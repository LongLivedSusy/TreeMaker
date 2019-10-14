import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9218522E-A8C1-E611-8A98-FA163ED7E46C.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7A6F40D0-ABC1-E611-9E9D-001E67C9B1BD.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/049973FB-ADC1-E611-838F-02163E015E87.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7469985A-B2C1-E611-AF04-FA163EE41CDB.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F6395682-B1C1-E611-AAAD-FA163E56B2A1.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/662E4C5E-B2C1-E611-BB67-02163E015CF6.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/18A5359B-B3C1-E611-82C6-FA163E0169F1.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5013D43F-BBC1-E611-9293-FA163ECCB736.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/AAA68C3A-06C2-E611-AC83-02163E00B86F.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5CB918C1-15C2-E611-A506-FA163E69F2C3.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0C3FD1BA-E1C2-E611-8CE1-02163E017F81.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4E653BC5-E1C2-E611-999C-001E67505815.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A292AFA5-02C2-E611-AC2F-A0369F7FC210.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5ED31B87-08C2-E611-9AB9-008CFA111200.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B62DB372-0FC2-E611-A4C4-00266CFCC23C.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3A7FED30-DCC2-E611-9595-A0369F7F9BE4.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/76B58E84-85C1-E611-9982-00259020097C.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F2AEBE47-E5C1-E611-B1DA-001E6779286A.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2CF10A62-02C2-E611-BB04-6CC21739C400.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8A07E163-B5C2-E611-9A19-6CC2173BC7B0.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/A89EC679-BEC2-E611-9CE4-6CC2173BC370.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9607BE3F-D2C2-E611-9054-6CC2173BC1A0.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3860C664-D2C2-E611-A080-C4346BC8C310.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F6C5FFEB-D4C2-E611-831E-C4346BC076D0.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3C84653B-D5C2-E611-ADA7-6CC2173BC1A0.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6A4D30FF-E0C2-E611-B1CB-6CC2173BB810.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/96BD94D6-EAC2-E611-A4A2-6CC2173BBF00.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FCD8DB30-90C3-E611-B532-6CC2173BBF00.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/42C94C6B-0AC2-E611-B8AF-484D7E8DF107.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D0842F9D-E2C2-E611-B9FF-001F2908EC96.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FC3B35C6-FEC1-E611-9DAE-FA163E260E18.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7C5DB429-02C2-E611-A98E-02163E013505.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7691F645-11C2-E611-877C-02163E0133A7.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EAD675C6-07C2-E611-AD2C-002590DB92BE.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/785466AF-0EC2-E611-A4AD-0CC47A7FC416.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2894CC6C-3BC3-E611-B136-70106F4A920C.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E02E72C4-3BC3-E611-831E-0CC47A7FC7C0.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/687A3727-3BC3-E611-B37F-0CC47A7E00C2.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B481EFA7-3BC3-E611-A9CE-047D7BD6DF2A.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/80A0E2A2-3AC3-E611-898B-70106F4A920C.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/144AF0D3-3BC3-E611-8CC8-0CC47A7FC716.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2EE53994-3BC3-E611-B68D-70106F49CDF4.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7C90B4C5-3BC3-E611-BABF-F45214938700.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/02C9C87E-9BC3-E611-A103-70106F45D198.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4200463B-95C3-E611-AA7C-C4346BC75558.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E037CBC8-9DC3-E611-BA98-C4346BBCB6A8.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C8C79CBB-03C2-E611-8DA0-001D09FDD6A2.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/12F4B8A0-D1C2-E611-81D9-848F69FD2904.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/08267D1A-08C2-E611-AF41-00259073E4DA.root',
'/store/mc/RunIISummer16DR80Premix/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F4D9AC7A-3BC3-E611-9488-001E67E6F512.root',
] )


























