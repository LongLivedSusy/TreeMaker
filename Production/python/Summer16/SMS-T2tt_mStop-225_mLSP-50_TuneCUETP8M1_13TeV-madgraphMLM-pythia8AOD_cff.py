import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/50662250-A1D4-E611-92D9-1866DAEA6D08.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C032E050-A1D4-E611-8412-1866DAEA8178.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FCBADBC6-A2D4-E611-9841-1866DAEEB0C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C8126BB3-A3D4-E611-87F5-14187741278B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5677872A-A5D4-E611-864A-1866DAEA6BC4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/903A7F57-D8D4-E611-AA44-B083FED42FE4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4466CBE2-99D4-E611-8945-001E67D8A423.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/24E3C7CA-9ED4-E611-9766-001E67DDC051.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0AFF0B41-D8D4-E611-AA4D-001E67A3EBD8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E84DA992-6CD4-E611-A330-0025905B8610.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/98ED1EA4-6DD4-E611-ACE2-0CC47A7C3636.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8649927E-6CD4-E611-9B56-0CC47A7C3472.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C4FA3DD3-6DD4-E611-BD55-0025905A60CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CEED6EC1-6FD4-E611-B192-0CC47A4D7600.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C86AD8B2-A2D4-E611-A30D-0CC47A4C8E70.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/36CCF7A5-A2D4-E611-9E5A-0025905A60E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9A6523C0-91D4-E611-8C10-02163E00E5D7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6645DDB1-94D4-E611-A34F-02163E00B837.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/660BB757-9FD4-E611-AA5E-FA163E852154.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E859ED58-A6D4-E611-BB7B-02163E013DE9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B0F27767-98D4-E611-9F4D-02163E0114AB.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/841F60D9-B0D4-E611-B242-02163E013DB2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7A9DA09D-B5D4-E611-8A07-FA163EA79AEE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2CAB1BA4-B5D4-E611-B0AD-FA163E93D6B9.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D8F72F99-B8D4-E611-8CBA-FA163EA79AEE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9E8D2643-B7D4-E611-981D-02163E015F8E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6E0F13DF-B9D4-E611-B485-FA163E9AD52A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8AEA6B7E-BBD4-E611-ADE5-001E67579ED8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0C9CAE00-B4D4-E611-9DE6-02163E00BDDD.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E88B3881-BFD4-E611-A713-02163E00C1C8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3265A2EB-C2D4-E611-AE4B-001E67C9B0A5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/28C08728-C8D4-E611-A1B2-FA163E12AAD8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5C3CBF4E-D8D4-E611-8019-FA163E54EC59.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/087DB7D2-D8D4-E611-94E2-02163E0138D7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C6CC64CD-FAD4-E611-90A5-02163E011503.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/34F5DE97-66D4-E611-AC92-0CC47A4D766C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2EC8BB76-65D4-E611-B9F5-0CC47A78A30E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8C9961D5-68D4-E611-A231-0CC47A4D76D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/2CCF957E-65D4-E611-A0ED-0025905A60CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A09D5E5F-6AD4-E611-81DA-0CC47A4D767A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DE862AE4-6AD4-E611-9CB5-0CC47A78A30E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/4E15300D-6BD4-E611-828C-0025905B8606.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B60F4E81-6CD4-E611-8D43-0CC47A78A426.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0EBD0C8C-84D4-E611-AB7C-E0071B7A9800.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4E417C4A-92D4-E611-9349-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8AA42E24-99D4-E611-B623-5065F37D0152.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EE7934D1-A2D4-E611-B287-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EE1D1035-D8D4-E611-9930-24BE05CECB51.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/480C5084-92D4-E611-B893-0CC47AA9906E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/22B85980-98D4-E611-A54B-0CC47AD99062.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A6F3DF80-98D4-E611-815E-002590E39D90.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9E5424E2-99D4-E611-A237-0CC47AA989BE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A8519DC5-9AD4-E611-A6FD-0CC47AA9906E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/987F2AAE-9DD4-E611-965D-002590EFF972.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CAFFB643-A1D4-E611-A9E0-0CC47AA9906E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BAB452AD-B0D4-E611-8A70-0CC47A13D216.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DC781951-D8D4-E611-ADFF-008CFA1112A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B0E23D0A-77D4-E611-A4C2-0CC47A7C3610.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C49DD4CF-7DD4-E611-9D92-0025905A6122.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/140E8D54-80D4-E611-A955-0025905B85CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F825596A-7FD4-E611-9096-0025905A60FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6C780F47-80D4-E611-89A6-0CC47A745294.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9C245C50-80D4-E611-A103-0CC47A4C8E66.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3CFABD86-81D4-E611-988B-0CC47A78A3D8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/88129F7D-81D4-E611-85AD-0CC47A4D76B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DCC41281-81D4-E611-A39C-0CC47A4C8E66.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/88127867-82D4-E611-97B1-0CC47A4D75EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DACF8689-83D4-E611-8FB0-0CC47A4C8EB6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/42C8A186-83D4-E611-9289-0CC47A7C35B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AE7BB780-81D4-E611-9656-0025905A6070.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3869794B-82D4-E611-B9DA-0CC47A4D76A2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E44A1782-7FD4-E611-9445-0025905B8600.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4428E64F-82D4-E611-8836-0025905A6064.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/765F54C9-86D4-E611-9493-0CC47A4D764A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7C4F00BB-84D4-E611-BB36-0CC47A78A30E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A2D0CD59-85D4-E611-920C-0025905A613C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5607B778-83D4-E611-A4B1-003048FFD7AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B4FA6F5B-82D4-E611-ABAD-0025905B8590.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B0BB1290-84D4-E611-A2C4-0025905B8574.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9092AEE7-84D4-E611-BB26-0025905B85CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BC68E5E9-8AD4-E611-AC44-0CC47A78A30E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5E72DDD6-86D4-E611-96C7-0025905A48F2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FEF841C4-86D4-E611-B77E-0025905B855C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2C5E42F0-8AD4-E611-A6E7-0CC47A4D7644.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FECD5663-85D4-E611-9BA1-0025905A60A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B62CC4AA-8CD4-E611-B0D8-0025905A60CE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/862CD79E-83D4-E611-AA1E-0025905B85B6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2CF440AF-8CD4-E611-B396-0025905A6122.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DE0A9915-92D4-E611-B0C2-0CC47A4D7678.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6ED4A221-91D4-E611-89D5-0CC47A4D7644.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0432FD63-97D4-E611-8FC9-0025905B85C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6C92F845-97D4-E611-8907-0025905B85EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E8E4064A-9DD4-E611-9ACA-0CC47A4C8E86.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8291D74B-9DD4-E611-A5F7-0CC47A4C8EA8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5EA22648-A1D4-E611-93BE-0CC47A4D7662.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3478C750-A1D4-E611-A587-0025905B8562.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8E80A49C-A2D4-E611-82B9-0025905A60CA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6C9C467D-A3D4-E611-AE04-0CC47A4D7626.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9EB89A80-A3D4-E611-A22A-0025905B85B8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/8CD75748-A3D4-E611-9F74-0025905B856C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/52F9556E-A6D4-E611-8C17-0CC47A745284.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/569D6CF4-A7D4-E611-9C2A-0025905A60A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/CA6B2EAB-ABD4-E611-BF2D-0CC47A4C8EE8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E4F1AB04-ADD4-E611-A72C-0CC47A78A2F6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1A899D92-B0D4-E611-9353-0CC47A7C35E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2015D434-AFD4-E611-BC03-0025905A6126.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/36EBCCB2-B0D4-E611-94C0-0025905A60CA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E0A74DE3-B1D4-E611-A5A8-003048FFD798.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0C4B4025-B3D4-E611-B7F7-0CC47A4D768E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/66C0BC74-AED4-E611-BB21-0025905A48E4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3ECA6D94-B0D4-E611-B6C5-0CC47A7C351E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EA986898-B4D4-E611-AC6B-0CC47A4C8EA8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/664E9642-D8D4-E611-94E3-0025905B85C6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DA6CCA80-D8D4-E611-8654-0025905B860E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-225_mLSP-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C42F0E4A-D8D4-E611-8533-002590D9D990.root',
] )
























