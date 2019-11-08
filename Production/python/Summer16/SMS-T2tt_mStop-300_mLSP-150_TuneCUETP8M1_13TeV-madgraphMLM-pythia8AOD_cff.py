import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/B2E6252A-17C7-E611-97A8-A4BADB1C5E28.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/50CE7A7E-1AC7-E611-AC64-549F3525A64C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1E0B3C8A-1AC7-E611-A7D0-842B2B42D35D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A0A097D8-1CC7-E611-A547-1866DAEB5C78.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/DC0FC6F4-1CC7-E611-8B70-549F3525DB98.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4622DDE3-1CC7-E611-8834-B083FECFEF7D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/F29A814F-1FC7-E611-B33B-141877410B4D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/AC626FD8-21C7-E611-807F-14187741013C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/08AFA14B-24C7-E611-B79F-1866DAEA8808.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1048EBAE-21C7-E611-9AD4-1418774118F6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/5E739A98-23C7-E611-B6ED-549F3525C380.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4E31CFC1-21C7-E611-9B31-90B11C0BDC70.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A06BB5BD-21C7-E611-AF4B-B083FED42488.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1AA3B351-24C7-E611-BFCE-141877410B4D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/3065A09C-23C7-E611-84B6-0026B93785EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/025A48BF-23C7-E611-AADF-549F3525B154.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/98CF35C5-1FC7-E611-831A-782BCB539B52.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D8389990-1FC7-E611-873E-90B11C0BD86E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1C305E1F-27C7-E611-A419-842B2B1811D7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D441AE1E-27C7-E611-B710-90B11C0BCF43.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/243381B7-29C7-E611-9C1C-1866DAEA7E64.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/26775EDF-29C7-E611-8DAD-141877410B4D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/327ACCDF-29C7-E611-A54D-141877410B4D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4872763B-2AC7-E611-A160-782BCB50BA54.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/464DD85F-2AC7-E611-BDE2-549F3525B154.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D85B709D-2CC7-E611-93F4-842B2B1812E7.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1871AF95-2CC7-E611-9FB7-549F3525C4EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/30E5E0E1-2CC7-E611-89AA-90B11C0BB9CF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/9686FEAC-2DC7-E611-A3E2-141877412793.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/505E4EE9-2DC7-E611-AC30-141877411936.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/1A82B516-2EC7-E611-A423-842B2B42BC3A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/46B1C175-30C7-E611-898C-141877411FED.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A89A0655-1BC7-E611-B979-001C23C0DF83.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E2BD20EF-31C7-E611-BD3F-001EC94BA3CC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2tt_mStop-300_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/361B5872-43C7-E611-99A8-001EC94BA119.root',
] )































