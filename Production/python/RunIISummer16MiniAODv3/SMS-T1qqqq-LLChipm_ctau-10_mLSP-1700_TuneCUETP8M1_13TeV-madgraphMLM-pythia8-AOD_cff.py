import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/A2835D29-D38A-E911-93B3-FA163E52A138.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/D4F99E03-D38A-E911-84DA-FA163E666D83.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/B60DC5DB-C986-E911-AFBB-14187741278B.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/38F17A5C-B987-E911-A9DF-20040FE8E90C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/94A844B6-CD87-E911-9A45-1866DAEB1FCC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/7C359A3D-1C88-E911-BCF8-90B11C0BCF42.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/5CD96795-1487-E911-AE96-B8CA3A709028.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/A297058E-3D87-E911-803B-A0369F30FFD2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/24D63FAB-1A88-E911-8612-B8CA3A70B608.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/DA2B2461-1A88-E911-AD41-001E6757E05C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/4C66989B-C487-E911-86CB-008CFAE45248.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/E0BC43DE-1888-E911-8CE5-008CFAC93DF0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/1C46729B-FA86-E911-871B-38EAA78E2C94.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/88E10232-C187-E911-8DED-38EAA78D8AD0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/3276E314-1988-E911-AB9A-0CC47AF9715C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/B08DEB93-1A88-E911-AFD1-D48564593FD8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/D61AA021-0D87-E911-B8A8-002590494C8A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/72DACB26-E086-E911-9060-0CC47A7FC746.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/64BB4615-E086-E911-85F0-00266CF3E4E0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/E667F910-0887-E911-B3D8-0CC47A7E6A74.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/327AD26E-1387-E911-8741-0CC47A7E6B00.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/86094290-2187-E911-B4BC-0CC47A7FC702.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/0A63555A-1588-E911-9C69-002590DE6E1E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/0A809C01-1988-E911-A77F-40F2E9C6ADD2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/A013ED49-DB8A-E911-A246-E0071B7B2350.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/74517080-E087-E911-816C-0425C5DE7BEE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/5C461A80-FA87-E911-A2F6-68CC6EA5BDF2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/5A9D9BF0-2188-E911-8003-90E2BAD1C730.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/D8FA7CDC-2D88-E911-AEBB-AC1F6B8DD212.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/5667A4E5-EA87-E911-AE78-0017A4771054.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/5E31E404-AB87-E911-A579-FA163E9F39BC.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/7CEB5F3C-C686-E911-A3A4-0025905A607A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/04EFA110-FC86-E911-A80D-0CC47A7C34C8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/80930A4A-0287-E911-88E3-0025905B8566.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/D28C4724-2287-E911-8C2F-0025905A611E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/9AFA7D52-CD87-E911-95C2-0CC47A7C3404.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/70000/A25A569F-698B-E911-93E7-0242AC1C0500.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/BCC9FA80-E087-E911-A7E1-002590DE6E72.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/4A5A4344-0787-E911-B20D-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/00265328-0A87-E911-89DD-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/162EF8D8-0987-E911-9381-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/D86A2322-0A87-E911-81EC-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/B449B0B9-1187-E911-8DD3-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/8EE70E00-BD87-E911-98CD-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/60617F3E-D187-E911-AA1D-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/28E47863-D187-E911-B4D7-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/82AD595A-D187-E911-B55D-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/4E51BF04-DE87-E911-BD11-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/3CCE3D07-DE87-E911-BFAC-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/36157D0C-E087-E911-BA41-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/369765C0-7B87-E911-AFCE-AC1F6B0DE0BA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/94CBB17A-C487-E911-8192-AC1F6B0DDFC6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/34CCDB2B-DA87-E911-90DF-0090FAA573B0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/C24AF268-1A88-E911-89C3-A0369FD0B11E.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/56AEA284-1A88-E911-AEA0-28924A3504DA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/4819773E-F486-E911-9A5B-0242AC1C0506.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/C6EBA06A-1A88-E911-AA1F-0242AC1C0501.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/5CEF32D0-C587-E911-A843-001E677923DE.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/24B73264-1A88-E911-928A-001E67792740.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/2ACDAC06-B186-E911-98F8-0CC47AFF02C8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/BC9E93EE-C986-E911-A288-0CC47AFF0468.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/0E35AAE5-C986-E911-9C7B-0CC47AFB7D80.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/264B7AAC-6887-E911-9FD4-0CC47AFCC6D6.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/12652137-D187-E911-9595-0CC47AFF02C0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/F2B55ED2-D687-E911-89D1-0CC47AFF0294.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/2C4F8C88-1A88-E911-919F-0CC47AFCC416.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/E65F881A-BD87-E911-B3C6-AC1F6B0DE2FA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/E2C87A7E-1A88-E911-A3A4-F4E9D4AF8BA0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/06DC783C-7887-E911-87D4-B499BAAC0414.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/ECC2A18F-1A88-E911-A993-001F29087E0A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/ECFA2198-7288-E911-97FB-00266CFFC664.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/70A61FD3-7388-E911-B8C9-00266CFFBDE8.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/B016C275-8888-E911-B72D-B026283D9D20.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/42437072-8888-E911-8609-B02628342360.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/EA8D7E48-4987-E911-8083-001E67DDD0AA.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/426757BF-7188-E911-978D-0CC47AA53D5A.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/6E8BFC14-7288-E911-BEE4-0025901AEDA4.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/D8D2AE63-0787-E911-AD7C-90B11C2ACF20.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/BA9BD9EE-1888-E911-ABA0-0025901D0C54.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/9CCF5682-D487-E911-93D9-00266CFCCB8C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/2E01E896-1A88-E911-9CE8-008CFA06473C.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-10_mLSP-1700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/1492D036-DA87-E911-BE7D-1866DA89061C.root',
] )
















