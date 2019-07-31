import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/509712C5-8DBB-E611-9C2B-0CC47A0AD63E.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/548A51A2-8EBB-E611-B7B1-001517FAAB30.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4A790A12-A4BB-E611-871C-001E67DDC0FB.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C4B4A9C5-6DBC-E611-B102-001E67DDC2CC.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BCB7E9C0-8DBB-E611-A0BF-001E67457A5D.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8650A775-8BBB-E611-AF90-0CC47A7C34A6.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4C09807D-8BBB-E611-B55A-0025905A607E.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6C30AE65-8DBB-E611-8DD7-0CC47A4D76A2.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6ED4E522-8EBB-E611-8044-0CC47A4C8EE8.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D2DA0E6D-8DBB-E611-B439-0CC47A4C8E66.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2A81DFF1-8EBB-E611-8A6E-0CC47A78A456.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/D413CFA1-8FBB-E611-B6A2-0CC47A745294.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4C87DEA1-8FBB-E611-9FB6-0CC47A745294.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/644FA22E-91BB-E611-9311-0025905A608C.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BC1024D6-99BB-E611-A272-0025905A60AA.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F48E17EA-A4BB-E611-A087-0CC47A74524E.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9C766CFB-A4BB-E611-9DA6-0025905A6104.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F08BC5DE-A9BB-E611-98B0-0CC47A7C3422.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/327AC682-6FBC-E611-AB85-0CC47A78A2F6.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/823B2195-7DBC-E611-BE97-0CC47A4D7674.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7C71E6A2-7FBC-E611-A6C7-001E674FCAE9.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/322F1B2B-96BB-E611-8A7B-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/88E66DAD-6CBC-E611-B0A9-0CC47AD9901C.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/50BF5017-A3BB-E611-9F72-002590FD5A4C.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2689588B-B9BB-E611-B9F7-0CC47A57D086.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/04E149AF-86BC-E611-9578-0025907DE266.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C43AC051-AEBC-E611-806B-0CC47A0AD6E0.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0E1C4941-A2BB-E611-B601-A0369F3102F6.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/AABBE3D7-A3BB-E611-A5DF-5065F3815281.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2A37AA11-A3BB-E611-A3A2-24BE05CE3EA1.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2000E512-A3BB-E611-BCEF-24BE05C656A1.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/16BD5814-A3BB-E611-8DCA-24BE05CE2E81.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F6484214-A3BB-E611-BDC2-24BE05CE3C91.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/74D0C319-A3BB-E611-BFA6-B8CA3A70BAC8.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3C0CC3E3-A3BB-E611-B17C-A0369F30FFD2.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4E878D93-B5BB-E611-AF34-5065F381C1D1.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8C5D189D-7FBC-E611-93A5-24BE05C488E1.root',
#'/store/mc/RunIISummer16DR80Premix/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2ED3B246-6FBC-E611-9E68-141877411367.root',
] )




















