import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8C56BFB0-94C1-E611-AC9A-A4BADB1E6031.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/08207E3D-5EC1-E611-B5D7-001E67457DFA.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BE5CC04E-91C0-E611-BE1C-0CC47A7C3408.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9EF34AE5-94C0-E611-9DB5-0CC47A4D7698.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AE40B00E-95C0-E611-9CBF-0CC47A7C3638.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C014AF0D-93C0-E611-9BBD-0025905A609E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4040AA9B-95C0-E611-9637-0CC47A4D7690.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6A718298-97C0-E611-B4AF-0CC47A4D768E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1E5B409C-97C0-E611-84D3-0CC47A78A2F6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/34E92C1D-9AC0-E611-8F77-0CC47A4D7650.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/92D5A536-9AC0-E611-A4C7-0CC47A4C8EEA.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4E335A26-9BC0-E611-B8A6-0CC47A4D7698.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BC853D32-9BC0-E611-B568-0CC47A78A4A6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B8C30894-9DC0-E611-A21C-0CC47A4D7632.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2015E378-9DC0-E611-8827-0CC47A4D76CC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FC8D9DA1-9CC0-E611-926D-0CC47A4D7630.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8CD27C64-9EC0-E611-85BF-0CC47A7C3636.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/58D31616-9FC0-E611-945C-0CC47A4D7646.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3E71C916-9FC0-E611-AC64-0CC47A7C340C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C4086241-A0C0-E611-A9B6-0CC47A78A408.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0C2ECF33-A1C0-E611-9A9C-0CC47A4C8F12.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/684CA9BD-9FC0-E611-BB12-0CC47A4D75F2.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/84AAD7D7-A0C0-E611-B47F-0CC47A7C3612.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/10C158FC-9EC0-E611-8933-0025905B8604.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7454216A-A3C0-E611-9872-0CC47A78A426.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FEF6A13C-A1C0-E611-948C-0CC47A7C3458.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3E144748-A2C0-E611-BF16-0025905A48F0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0607984D-A0C0-E611-BFCC-0CC47A7C347A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C42C0276-A2C0-E611-BF9C-0025905A6138.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/18D56408-A2C0-E611-BB9B-0025905B85DE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/00890363-A8C0-E611-8451-0CC47A78A41C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/22EC6E18-A8C0-E611-B072-0025905A6092.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/EE5D4E85-72C1-E611-B34A-0CC47A78A4A0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DC7EDC1C-75C1-E611-ADFF-0CC47A78A2EC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA870BD3-C1C0-E611-A6A7-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9C69ACCF-5BC1-E611-97BC-0CC47A13CDB0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/249117FD-8CC0-E611-A02A-FA163E749F89.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C016A8FF-8CC0-E611-ACFF-02163E013DD6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3AAF4380-90C0-E611-ABBC-FA163ECBC3A4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9A74C95A-92C0-E611-BB9E-02163E01647B.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C8BDA890-92C0-E611-8D93-0025901E606C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/803F8DBC-93C0-E611-829F-002590495074.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DA66CB9B-95C0-E611-932F-001E67C9B44C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FC5547C5-93C0-E611-B3C1-02163E00BC46.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/907B2FCE-93C0-E611-9854-0CC47A044870.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/963F9C3C-99C0-E611-8D09-FA163E4FC583.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/22C1A697-94C0-E611-A503-02163E00B316.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2E3F0D9C-95C0-E611-BEDC-0025901E606C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/34DE9A14-9AC0-E611-99EE-2C600CAFEE64.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/50018B40-99C0-E611-9792-02163E015F80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/62F8B5A7-94C0-E611-9613-0025904B1F90.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1A0CA3B9-9CC0-E611-804B-FA163ECBC3A4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CC61638D-97C0-E611-BAB7-0CC47A04488C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A2F812B2-97C0-E611-9DDA-02163E00C914.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9C2DF668-97C0-E611-96E5-02163E00BDB8.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BA5F6F4A-9CC0-E611-8F85-002590494FEA.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A4C57E2C-A1C0-E611-90E6-FA163E4BD49B.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/62EC50C4-A2C0-E611-8F06-FA163E161622.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7E20EC97-A2C0-E611-9179-002590494E94.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/046D9DAE-A8C0-E611-B62D-FA163EDB11F7.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1C1070C5-6CC1-E611-98AE-02163E00B8A7.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/EEDCBAC0-73C1-E611-B8EC-02163E00B881.root',
] )










