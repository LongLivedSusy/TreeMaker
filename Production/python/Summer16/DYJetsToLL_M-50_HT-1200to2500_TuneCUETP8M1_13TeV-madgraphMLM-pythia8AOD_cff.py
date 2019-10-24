import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CE45A9A0-60BD-E611-B6BB-008CFAF750B6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/50542FF1-62BD-E611-BC31-008CFA002830.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C47BB997-64BD-E611-B6ED-848F69FD29B2.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D6A9FD16-66BD-E611-91F5-008CFAF0842A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/78F66318-65BD-E611-BCBB-848F69FD4565.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/28163ED8-64BD-E611-B343-848F69FD2817.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/70DAEB83-68BD-E611-AAC7-848F69FD4565.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FA7D2737-6ABD-E611-A9B1-008CFAFBE5CE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DA3AF14B-67BD-E611-AA03-008CFA0004B0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D6606384-68BD-E611-ADDE-3417EBE64B85.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/862E080A-6BBD-E611-8FE5-F04DA275BF11.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8465A7AC-6CBD-E611-A57C-848F69FD4517.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2E6C7FA8-7EBD-E611-8BB3-F04DA275C2FB.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/380CE41F-67BD-E611-B57C-B083FECFF297.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/104302FB-68BD-E611-8263-001EC94BA15F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/085DAD6D-6BBD-E611-9C6F-B083FECF837B.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/2028B0DB-6CBD-E611-9E15-A4BADB1E6796.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3CFAE1A9-6ABD-E611-824A-001C23C0F1F4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/24F9EAD6-70BD-E611-8AC1-782BCB539AB1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/E4740DC7-E5BD-E611-90C0-B083FED046D9.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/22290C6F-6BBD-E611-9119-0CC47A6C138A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/BAE85769-6EBD-E611-BFE5-90B11C2ACF20.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C8E3B224-86BD-E611-B157-0CC47AD98D00.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/46D554CC-E5BD-E611-8FE8-0CC47AA98F92.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/961769D0-E5BD-E611-AFAA-0CC47A57CDD2.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C04C8180-64BD-E611-ABC3-002590E3A0FA.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A09BFF7C-65BD-E611-B8FC-0025904A9472.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/24A91362-67BD-E611-941B-0CC47A6C06C6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/76F6EF69-66BD-E611-B502-0025904AC2CC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/148C12AD-68BD-E611-8460-002590E39F4E.root',
'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BA51A278-6ABD-E611-9D6B-0025904A9472.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/243CF1E1-6CBD-E611-BD6C-0CC47A13CCFC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A4C875A2-70BD-E611-8E34-90B11C27F89E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FC6A97A6-3BBE-E611-9DF2-0CC47AA992B4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BA1229E7-C6BE-E611-B994-0CC47A13D416.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9C2CDDA0-7BBE-E611-8B84-00259073E4E2.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/520D9FCA-E5BD-E611-A571-B8CA3A70A520.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8E3728C7-6DBD-E611-B7A6-00266CFEFE1C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA26A67E-39BE-E611-8530-6CC2173BBF40.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DE718CC8-5FBD-E611-9C87-141877410340.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4E087564-61BD-E611-B277-782BCB1D28F8.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/201F94C6-60BD-E611-957E-782BCB539AB1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AE6263CE-62BD-E611-8B67-B083FED42C03.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/48433FE0-63BD-E611-B0A7-141877343E6D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D08647A2-64BD-E611-BEB4-782BCB20D86D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/04A19987-66BD-E611-83DF-1418774108DF.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E86C5A68-65BD-E611-BF10-782BCB206037.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5C879481-65BD-E611-8CDD-782BCB1D28F8.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/38BD6523-68BD-E611-87EA-1866DAEA6CC4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3E03AB78-68BD-E611-805C-1866DAEB1FC8.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/64AA9E5E-67BD-E611-8D0A-B083FED42FB0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/60AC135F-67BD-E611-ABF6-141877343E6D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/562A6E68-67BD-E611-8894-A4BADB1E65B1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3CA66E5F-68BD-E611-952D-1866DAEECF18.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1AF09986-66BD-E611-A4EC-90B11C0BCF43.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/529C8408-6BBD-E611-BE0E-141877343E6D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AE67BD9A-64BD-E611-B629-0019B9CAB9CB.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FA689F27-6CBD-E611-80D3-1866DAEA7F94.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FCF6C212-69BD-E611-9F24-782BCB539ABA.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/263677CC-69BD-E611-9230-782BCB539AB1.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6A9782E6-6CBD-E611-B6CD-A4BADB22A387.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA53CA03-6EBD-E611-A77B-1866DAEA7F94.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3A3CFD55-72BD-E611-8E55-D4AE526DF2E3.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BC4981AA-3BBE-E611-A47B-141877411367.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7C74F4CA-E5BD-E611-8B0B-001E67A4061D.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/8683F4AD-E9BD-E611-93F8-0242AC130003.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E42D8400-81BE-E611-A07C-002590E7D7EA.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3090700B-C7BE-E611-A886-001E677926F8.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B43FBF72-DEBD-E611-AFCF-FA163E7A20D7.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B6F577D3-DFBD-E611-B936-FA163E40486E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BE902AD5-E2BD-E611-BC88-FA163E1A09F8.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D856D969-AABE-E611-B3AC-02163E01306F.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2E3F3A87-ACBE-E611-B96E-FA163E6A32B0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3CD9251D-42BE-E611-937F-00304867FE73.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3A05E5EA-C6BE-E611-9B84-70106F4D2378.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7C31A19D-7CBD-E611-B394-0025905A60E0.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8E094B78-7CBD-E611-B81C-0025905A6092.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/32689CA1-7CBD-E611-B5D6-0CC47A7C34E6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/40AC2C6F-7CBD-E611-A607-0CC47A78A45A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1217486C-7CBD-E611-8FC0-0025905A60DA.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/847AC96A-7CBD-E611-9F47-0025905A612E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0C77DD7C-7CBD-E611-BCC7-0025905A6092.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9E29BEA2-7CBD-E611-8565-0025905B857C.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E01F913A-89BD-E611-8A06-0025905A605E.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/22A3FF3D-89BD-E611-A9F4-0025905A6138.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FA5C6AE4-B8BD-E611-A85E-0025905B8566.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/52D80270-BCBD-E611-9869-0CC47A78A340.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E439C3D6-BABD-E611-B0F3-0025905A60F4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F8D0CA6C-BDBD-E611-A47B-0CC47A7C357A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/98934572-BCBD-E611-8B2D-0025905A60C6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/22C8691F-BEBD-E611-9E8D-0025905A60FE.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8C32C81D-0ABE-E611-B052-0025905A48EC.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CAD187E3-15BE-E611-BB3E-0CC47A4D76B6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DE4257AA-86BE-E611-B9A2-0025905A6080.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AA4DC528-91BE-E611-8541-0025905A60E4.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/528168E2-94BE-E611-BCE3-0CC47A4D76D6.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/42801B52-97BE-E611-B9DD-0025905B8582.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2683D6B0-9BBE-E611-A39D-0CC47A4D7674.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/84664ED8-A1BE-E611-85A2-0CC47A7C3638.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DEAE06FF-A2BE-E611-8B25-0CC47A74527A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/00BA9D16-C7BE-E611-B3D7-0025905B8572.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/36F041F2-C6BE-E611-911D-0025905B858A.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FE49B693-6DBD-E611-BA45-24BE05C3EC61.root',
#'/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B4B632E0-C6BE-E611-BAC0-A0000420FE80.root',
] )





























