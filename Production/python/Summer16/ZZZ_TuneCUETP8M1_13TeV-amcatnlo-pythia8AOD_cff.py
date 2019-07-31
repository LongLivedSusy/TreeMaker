import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0C68858C-FFBE-E611-A90C-FA163E3CB127.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/364B4795-FFBE-E611-9D06-FA163E73FE13.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7CD8C88B-FFBE-E611-8538-00259075D714.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1AC7D0EC-74BD-E611-8D54-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D411C63F-78BD-E611-AF01-0242AC130003.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C8DDAE36-74BD-E611-B5F3-ECF4BBE1CEB0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7C3C939C-76BD-E611-9E5D-D067E5F9184E.root',
'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/10D45BAF-79BD-E611-A546-001E67586A2F.root',
'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F8B26EFF-86BD-E611-AEC5-001E674FB207.root',
'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9CCF2A57-34BE-E611-8FCE-ECF4BBE16338.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0C65DB84-FFBE-E611-9970-D067E5F90FB1.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2E4072AC-90BD-E611-B2B7-001E67DDD22B.root',
'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/78F1EBC3-90BD-E611-BAF0-A4BF0102A5F9.root',
'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DE5394B2-90BD-E611-A170-001E67A404B0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D01B5286-90BD-E611-9E38-001517FB25E4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3EA29D0D-9CBD-E611-A227-001E67A40451.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/28915B54-6DBE-E611-A60B-001E67DDC254.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4077932A-8ABD-E611-AE3A-0025900E3514.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2AF53855-8EBD-E611-9456-0CC47AA98B8C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1EAF9D15-8EBD-E611-95CC-003048F7CC8A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6083CD6E-8FBD-E611-8F7E-0CC47A13CFC0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8C8DD1B4-91BD-E611-AFB3-0CC47AD99050.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/68AFD8E5-5ABE-E611-9DB0-0CC47AD98C86.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/74D69956-FFBE-E611-9818-0CC47AA989C6.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/162F551E-F1BD-E611-8D72-003048FFD75A.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6AF66A98-6DBE-E611-B5E4-0CC47A7C3636.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/10220207-FFBE-E611-B098-A0369F30FFD2.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4035C492-FFBE-E611-8ABD-0CC47A4D7646.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4871AD92-FFBE-E611-B19B-0CC47A4C8F1C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/ACBA25E0-8DBD-E611-A351-B083FED424C4.root',
'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D82B4D62-8DBD-E611-AF9D-B083FED14CE0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/283CD8CE-8FBD-E611-A4F0-D4AE527F2883.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/42FB0282-92BD-E611-823A-B083FED424C4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/04E64E9A-95BD-E611-B252-001EC94BA119.root',
#'/store/mc/RunIISummer16DR80Premix/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/58E64DFC-9DBE-E611-B30A-D4AE527EE7C4.root',
] )




















