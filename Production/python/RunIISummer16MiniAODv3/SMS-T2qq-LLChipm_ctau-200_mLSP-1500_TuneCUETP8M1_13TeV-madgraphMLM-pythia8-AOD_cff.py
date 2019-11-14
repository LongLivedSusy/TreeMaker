import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/84F5D5B6-0789-E911-9CCF-FA163EF2502C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/082EDEC1-778A-E911-86EB-FA163E764C5A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/509067BC-478C-E911-B7F0-A0369FC5E51C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/2E561F93-0A88-E911-87D9-002590DE7230.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/22E0FFC7-DF88-E911-9EAD-002590DE6E34.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/6263E073-1C89-E911-9A8F-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/5474F9D0-DF88-E911-AF42-20CF3027A684.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/92846940-428A-E911-B0F8-B026283450A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/D05655BA-4089-E911-9BB4-AC1F6B1AF01A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/3C4F5A70-2D8C-E911-B8E0-0CC47AFF04A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/E2721CA1-5E8A-E911-A645-008CFA110C68.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/1CB5CA96-478B-E911-B791-0CC47A1DF806.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/FE58CC30-CE88-E911-9CE2-6C3BE5B594A8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F6B30BA5-1C89-E911-A6A9-AC1F6B8DD244.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/54640558-6189-E911-B865-0CC47AFCC41A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/109FC702-3A89-E911-8A40-0CC47A4D7668.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/8E4A65F0-888A-E911-83C7-001E67E6F4FE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/0E0C599E-148A-E911-884B-0242AC1C0500.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/9AF71EA8-5E8A-E911-83AB-EC0D9A8221EE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/D46DF340-738A-E911-A215-5065F3810301.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/EC9B6A02-5688-E911-9D3C-0242AC1C0507.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F241082E-4989-E911-9256-0242AC1C0500.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/022EFE54-3A89-E911-B9BB-00259019A43C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/805253C7-9A8C-E911-9C15-008CFAF5592A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/36EDB561-2C8A-E911-9DED-6CC2173C3DD0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/9EBCED83-5E8A-E911-BAA1-AC1F6B0DE0BA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/64FD3DEF-728B-E911-9F8D-A0369FD0B3A0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/28DA281D-0E8C-E911-9255-44A84225C8FF.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/AE189C9F-948C-E911-93B1-0CC47AFC3D32.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/72344949-9393-E911-ADDA-7CD30ACE23E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/E0BC1907-558E-E911-B80B-0CC47AFC3CA6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/2E667275-EC8D-E911-9273-A4BF01026229.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/6C61BD01-B190-E911-A67C-EC0D9A8222E6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/B2651D0C-0290-E911-B470-0CC47AA98D60.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/769E69EC-F68F-E911-9B40-001E67DDBFC5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/4EC778C7-CC8D-E911-A2B3-F4E9D4AF72D0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/2818E215-768E-E911-8A52-E0071B6C9DE0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/1E213B6F-6B92-E911-87E4-48D539D33331.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/C6185F12-E890-E911-9780-AC1F6BABF8D5.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/2A1FD189-1691-E911-8599-008CFAE4545C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/A88999ED-F38F-E911-AF24-7CD30AC0311A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/34D42306-9A93-E911-92EE-0023AEEEB208.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/D66245F1-6F94-E911-AF4B-0CC47A5FBE21.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F25DD5D1-A090-E911-963D-B02628341EE0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/C80E17B1-AD90-E911-8138-509A4C748037.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/6A60520B-498F-E911-939E-0CC47AFF02C4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/6051F384-9D8E-E911-86DC-0CC47A7C3458.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/84EBA81F-D48F-E911-B1CA-0025905B856C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/32FDE016-1E8E-E911-B18A-0242AC1C0504.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/F05B847F-4E8F-E911-BE87-0242AC1C0502.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/88EFE5B2-4096-E911-9BEE-509A4C84EA1B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/7E4165BF-1F8E-E911-B8C8-003048CBA4EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/28836DF4-E78D-E911-AE36-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/C86DB281-F78F-E911-BDCD-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/D6F0F582-CA91-E911-B8FF-FA163EAA4686.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/C44CD213-A497-E911-80EF-549F3525C4EC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/229218E8-049C-E911-98E9-001D09FDD80D.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/8E316120-688E-E911-8D74-002264069120.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T2qq-LLChipm_ctau-200_mLSP-1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/40000/EAF71934-608E-E911-8EB5-98039B3B01CA.root',
] )











