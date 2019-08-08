import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/D26DA028-F1D1-E611-93FA-0CC47A13CFC0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C49AFD38-F1D1-E611-BE2C-001E67A3FF1F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0A344485-01D2-E611-BFA5-001E67A3E872.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F40DE449-DDD2-E611-B4EA-A4BF010255AE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/CA09D606-EFD1-E611-A58E-E0071B7AC5D0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/8CEDF62F-F0D1-E611-AA54-5065F3819221.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/4A20842F-F0D1-E611-80F6-24BE05C4D851.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/AEF5BCAD-F0D1-E611-97C4-24BE05C3EC61.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F8E24B55-F1D1-E611-9E1E-24BE05C4D8C1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/AAAA1F7C-F0D1-E611-81FB-2C4138EBDA9C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/58AD0058-F1D1-E611-84AF-E0071B741D70.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/DEF03158-F1D1-E611-83C2-E0071B741D70.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/346FCF0D-F2D1-E611-B275-5065F3815221.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/9C1B3AD9-F2D1-E611-958E-5065F381C251.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/80401BE5-F2D1-E611-875B-5065F3819221.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/EEE8182F-F4D1-E611-80C5-5065F381E211.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/7865CB0E-F2D1-E611-8A7B-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/0099BA0E-F2D1-E611-96C7-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/10391520-F4D1-E611-8383-5065F38162B1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/563D4D25-F4D1-E611-8732-E0071B7A8550.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6CB90760-FED1-E611-8A6D-E0071B7A8570.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A4063925-BED2-E611-A315-24BE05BD4F61.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/DE55FD22-F1D1-E611-8E0B-0CC47A4C8ED8.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/969B63CF-EFD1-E611-8FD0-0025905A612E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/86CE4B4F-B9D2-E611-907D-0CC47A4D765E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/4AC71931-BBD2-E611-99AC-0CC47A7C340E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FE2E640B-ADD2-E611-A15A-A4BF01013D80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/6442E050-C7D2-E611-90A3-FA163ED3C452.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C6EB688B-EED2-E611-9D2F-FA163E87EE6F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/62D91667-EBD1-E611-B59E-02163E00BAF7.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A638914B-F3D1-E611-B9FA-02163E017720.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC45B84C-F9D1-E611-8F11-FA163EDB1C0A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9ADEE3B6-FAD1-E611-9187-FA163E806E80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3C0AAD6F-C3D2-E611-B4E4-FA163E3E59F8.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/8646A985-CBD2-E611-93A2-FA163E0854B0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/12E4E68D-C0D2-E611-9CA0-ECF4BBE1DD48.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/0873BAEA-F7D1-E611-B261-002590D9D8AC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9EDF4841-BFD2-E611-85AE-008CFA197A04.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BC425411-B3D2-E611-8066-0CC47A0AD6DA.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EC8D5738-F0D1-E611-9DBC-E0071B7A9810.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A033B4E5-F5D1-E611-9881-5065F37D4131.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/2CA6541A-F5D1-E611-B3EF-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/7040721E-F5D1-E611-820A-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D8E10D1A-F5D1-E611-9642-2C4138EBDA9C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4E62EB18-F5D1-E611-BA58-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FC397070-BFD2-E611-BE44-24BE05BDBE61.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6A211AEA-00D2-E611-A8D3-001E674FBFC2.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0CB1620B-06D2-E611-B6BC-0242AC130005.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A6652E9A-02D2-E611-8C95-001E67348055.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DAE3AEE8-03D2-E611-9FDB-001E674FB063.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/745AFCA0-06D2-E611-ACFB-001E67457107.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/66CD9380-0CD2-E611-B216-001E674FB063.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C4B778C0-D0D2-E611-B06E-0242AC130003.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/92CFA427-E5D1-E611-B7CD-1866DAEA6CF0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/5CD9280A-F1D1-E611-927F-1866DAEA6CC4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/62202535-F0D1-E611-9758-549F3525A184.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/9AA7BCA9-F2D1-E611-B4A9-1866DAEA6D08.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B61F22FE-BCD2-E611-9467-782BCB20EBA4.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/3E229DB0-F6D1-E611-A48B-002590FD5A3A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/00971AF7-F6D1-E611-81A3-0CC47A57CE00.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/64C3CAA1-F7D1-E611-8F87-00259019A43E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/AA6A4F37-F5D1-E611-802B-002590D9D92A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/C0BC2AE1-F8D1-E611-978B-002590D9D8B6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/84968230-FAD1-E611-8E9C-002590D9D8B4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/981EC036-C4D2-E611-88F8-002590D9D880.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/B4B36006-E5D1-E611-B40F-0CC47AD98BEE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/467BDAE4-E2D1-E611-86BC-002590E2DD10.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CAF7B642-E4D1-E611-B4C6-90B11C2CB7A9.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F44F465C-E6D1-E611-A2AA-0025904AC2CC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/A0A08812-ECD1-E611-9CF3-1866DAEEB0A4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/28B12301-EDD1-E611-9C3B-44A84224BE51.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/BAB76618-EBD1-E611-8C94-B083FED3EE25.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/36E777E0-EDD1-E611-B65B-90B11C0BC870.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F4E6EB3E-EFD1-E611-AD1A-90B11C0BCE26.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/F2DAD311-F2D1-E611-BA41-B083FED4263D.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/6C00734D-F0D1-E611-9EFF-001C23C105FC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A68D4F3C-EFD1-E611-98A5-0CC47AD99062.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DC6C4B19-F2D1-E611-B72B-0CC47AD9901C.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/6C89E929-F1D1-E611-9B6E-0CC47A13CB36.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E0EC6735-F4D1-E611-BC3F-0CC47A13D2A4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/985DD22C-BED2-E611-B523-002590E3A0D4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/FE3905F0-F9D1-E611-966F-001E67DFFB4F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E4358A24-95D2-E611-9515-1418774108DF.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A252E64B-96D2-E611-B7C1-B083FED42ED0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/EE0CF211-FAD2-E611-900A-141877410E71.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BEC73720-E0D1-E611-A697-24BE05C6D5A1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/54A0CADE-EDD1-E611-A3C5-5065F381A251.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F61D9DC3-EED1-E611-86A8-5065F3820351.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3C761538-F0D1-E611-9061-24BE05C46B01.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/02398A36-EFD1-E611-B34A-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BC4BD53C-EFD1-E611-9D46-B8CA3A70B608.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/88ADEC6C-BAD2-E611-9270-24BE05C6D5B1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1A668839-F9D1-E611-A893-001E674FCAE9.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8484BF03-FCD1-E611-BD70-0242AC130007.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/045AFAEF-F7D1-E611-A310-001E674DA1AD.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/B8EC6856-FAD1-E611-BA9D-001E67348055.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2EDAC5C8-FED1-E611-82DB-001E674FCA99.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/025CB6C5-FCD1-E611-90C1-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FEFD3559-FBD1-E611-AC46-001E674FCA99.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/769F046F-FDD1-E611-867B-001E674DA83D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/D2BE954B-FBD1-E611-8B78-001E67457E9F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5A4077CE-0AD2-E611-B642-001E67457E9F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CE0BDDB8-FDD1-E611-B094-001E674FAF23.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/344C7E22-1AD2-E611-8760-D067E5F9156C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/084CA38A-27D2-E611-95AE-001E674FAF23.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CC760C95-2ED2-E611-8DD9-0242AC130004.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/62F871D9-2BD2-E611-8243-001E674FB207.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/58B8548C-30D2-E611-AF85-001E674FB149.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C0191C5B-7BD2-E611-8523-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/30CE9CD3-F3D2-E611-BFE7-001E674FC800.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C2055C2F-F6D2-E611-9160-001E674FB063.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C8CF89B0-FED2-E611-BF99-001E67586A2F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/86347180-0BD3-E611-B3A3-001E674FB24D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DC1CECD2-F0D2-E611-841C-0025905B8598.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/02D93C25-F3D2-E611-96B5-0CC47A7C34E6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/100000/14AC54C8-B7D2-E611-A8B0-008CFA1111AC.root',
] )






















