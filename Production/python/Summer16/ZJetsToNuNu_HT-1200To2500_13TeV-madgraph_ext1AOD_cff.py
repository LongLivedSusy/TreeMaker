import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/58C485A0-62C2-E611-BB84-0CC47AD98BC2.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/CC04D74C-60C2-E611-BE81-0CC47AD98BEA.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/D8A65BBF-65C2-E611-8E2C-0CC47AD98D0C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/EE8ACED5-64C2-E611-81B8-90B11C2CB7A9.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/FA0F7489-66C2-E611-A646-0CC47AD98C86.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/CE0DED29-67C2-E611-AA10-0CC47AD98BC2.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/A2957C00-69C2-E611-A502-0CC47AD98BEE.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/AEA56D60-6AC2-E611-B86D-0CC47AD991FA.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/8E8D130B-6BC2-E611-8B2C-0CC47AD98D08.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/2E1644B8-6EC2-E611-ADDD-0CC47AA98F9A.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/24786AAB-6BC2-E611-92DB-0CC47AD98F70.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/86336608-69C2-E611-AC83-0025904A9472.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/E458417D-6DC2-E611-A5E3-0CC47AD9908C.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/946DAD94-70C2-E611-9A13-0CC47AA992B4.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/C8EBA0FB-72C2-E611-9FAA-0CC47A13CD44.root',
'/store/mc/RunIISummer16DR80Premix/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/70000/DE8247A8-8BC2-E611-BD3F-0CC47AD98F6A.root',
] )

















