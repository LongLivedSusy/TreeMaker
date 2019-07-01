import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B0D71A03-14B3-E611-960B-001E677923F0.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4E871975-A1B2-E611-B95B-008CFAFBE8F2.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B0A4A55B-A5B2-E611-96EB-3417EBE64C7B.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1075D683-A8B2-E611-AE62-7845C4FC36E6.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/EC93E735-AEB2-E611-9A8C-008CFA0027B4.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0A7C8606-B1B2-E611-AA31-008CFAF75254.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C65F0F39-F6B2-E611-AD60-848F69FD4ED1.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/986069D1-F9B2-E611-8821-008CFAFBE5E0.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/985F061A-FCB2-E611-AD11-848F69FD4586.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DABA8024-FDB2-E611-A7CC-008CFAFBE5E0.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/909D1271-FEB2-E611-AA1D-008CFAF75602.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F8C56BD6-FFB2-E611-89BC-008CFAFBE5E0.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BC923291-01B3-E611-8859-F04DA275BFCE.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FEFAC7CB-04B3-E611-BE3B-848F69FD29D3.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1A8B2746-06B3-E611-A659-008CFA002830.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AEE3C994-0AB3-E611-AC28-008CFAFBF6CC.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5667DED9-07B3-E611-9C3B-848F69FD4EB6.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4E6B312F-09B3-E611-A3F6-848F69FD3EC9.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C074E4E1-09B3-E611-930C-848F69FD46C1.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1EA3ECDC-0BB3-E611-A40E-848F69FD3FAA.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DE65C03E-0DB3-E611-B4DF-848F69FD4E98.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/347F7B6D-0EB3-E611-8FF4-848F69FD4EB6.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B0D8AAD7-12B3-E611-9A13-848F69FD4EB6.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1EAA59E1-B1B2-E611-A2DA-008CFA56D770.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6C6054E8-19B3-E611-9184-549F35AF4517.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/40A9B272-6AB2-E611-9D9F-FA163E924F37.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5E20EDBF-A2B2-E611-B8E9-00266CFFCB7C.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DE5E9C38-A8B2-E611-82FC-6CC2173BBE60.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/368C3C4C-ABB2-E611-985E-00266CFBE43C.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0C2DC068-ADB2-E611-8902-C4346BBCD528.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3A6CD637-F6B2-E611-AFB9-00266CFFBCDC.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA29459F-FAB2-E611-BB10-C4346BBCB6A8.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9CCC8AA0-FDB2-E611-93B8-00266CFFC9C4.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0EF8E405-00B3-E611-BACA-001E67F336E0.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1ECA2D73-FEB2-E611-B6B2-00266CFFBF64.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2E5D0649-02B3-E611-9588-00266CFFC9C4.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E2C0131A-07B3-E611-A857-C4346BBCD528.root',
#'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B6D65230-09B3-E611-A6F0-001E67F336A4.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/ECB19BDD-0BB3-E611-985E-C4346BC70B58.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E015680B-14B3-E611-8239-00266CFFBF84.root',
'/store/mc/RunIISummer16DR80Premix/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C0FEF050-0EB3-E611-86D3-001E67F336A4.root',
] )











