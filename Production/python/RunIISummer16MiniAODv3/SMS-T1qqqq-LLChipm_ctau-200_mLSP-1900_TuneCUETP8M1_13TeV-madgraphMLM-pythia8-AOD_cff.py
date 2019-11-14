import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/F2591F07-DE87-E911-9A3E-001E674FD1F6.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/3A7FF468-E987-E911-AC0E-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/8202270B-B788-E911-B23A-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/5C6D5EBD-2889-E911-A8BC-008CFAE4504C.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/CAEB3DBE-DA87-E911-BEC9-D8D385B0EE2E.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/3A2DA382-EB87-E911-A7DA-6C3BE5B594A8.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/F03414FB-BB88-E911-B1F1-484D7E8DF0D3.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/2843B497-C187-E911-BCB5-0CC47A6C06C4.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/6234E66D-9288-E911-8324-0CC47AA992C8.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/DEB7E505-DE87-E911-A790-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/3AE98DC0-E387-E911-B2BF-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/E8C725FD-E187-E911-B05C-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/6857647C-D887-E911-93C8-20CF3028D5CE.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/F2B1D2F9-BB88-E911-9D38-B083FECFC6ED.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/4A2F01EB-EA87-E911-8A78-002590DE6E72.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/C4F09A36-2889-E911-B769-0CC47A706FF8.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/868662A9-B488-E911-802E-1CB72C1B6568.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/EEAEACBB-E187-E911-B6BC-0017A4771068.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/521BE0F7-A588-E911-8ABA-6CC2173C3E80.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/204FE135-2889-E911-9101-AC1F6B596102.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/54830AB9-EC87-E911-9468-549F3525B220.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/58D6A0AD-B488-E911-BF5A-20CF305B066A.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/D0212740-7587-E911-9537-008CFAC91BD0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/9A1C3ED1-7B87-E911-89E2-3CFDFE6A32C0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/6A9299D5-7B87-E911-83E6-008CFAE45344.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/FCDE67AA-8187-E911-A55B-008CFAC93DA8.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/C605C0E8-8187-E911-8F90-008CFAC93D10.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/C845D936-8887-E911-ABD7-008CFAC941C0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/6A399738-8887-E911-A843-008CFAE453CC.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/4A6CF436-8887-E911-B38E-008CFAE452AC.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/26BF9767-8F87-E911-9EBA-008CFAC91964.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/009008C9-BC87-E911-B41C-008CFAEBDA58.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/06C9A262-C287-E911-9D5C-008CFAE4523C.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/2A774F54-A287-E911-B337-0CC47A7C3430.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/028E1CF5-C287-E911-A678-0025905B85DA.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/48852648-E787-E911-B084-0CC47A7C34E6.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/4EF0AEB3-B388-E911-AE33-0CC47A4C8EE8.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/14CE5A3F-2889-E911-8422-90E2BACBAD58.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/1E619BA8-9A89-E911-A9D1-C0BFC0E56846.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/4E8295E4-2789-E911-877E-20CF3019DEF6.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/3EBD99DD-2789-E911-B828-C4346BB236C0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/5AD2AE37-2889-E911-9720-00259090909A.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/BAEA083C-C687-E911-A58F-0242AC1C0504.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/C22B4A8F-9C88-E911-BA38-0242AC1C0500.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/F05508E3-2789-E911-A4BE-0242AC1C0501.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/24C24E7B-9F88-E911-846A-A0369FD0B3F0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/14C2A857-2889-E911-8DAD-AC1F6B0DE490.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/1C9E7D59-C487-E911-9298-0026B9F8FDAC.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/D42D5F60-B188-E911-BC3A-44A842BFA958.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/70006B40-DA87-E911-BACF-0CC47AFF02B8.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/00FEE645-DA87-E911-9323-0CC47AFF0190.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/8ED7C2E8-DF87-E911-ACA6-0CC47AFF02EC.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/EE72A637-FD87-E911-9826-0025905C53B2.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/8E6B09D9-2789-E911-B7F4-0025905D1D78.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/8C95A0AF-DE87-E911-A66A-A0369FF88602.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/C66EBD54-AE88-E911-91DF-008CFA197B44.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/3C7AC375-8888-E911-B9CF-B026283D9D20.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/B07514B9-D488-E911-A67C-3417EBE64CDB.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/B4C547C2-2A89-E911-ABD6-7CD30AD08EAE.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/AC8924D2-2789-E911-9A70-E0071B73B6A0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/7AB0D73D-D487-E911-B6D7-FA163E995D02.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/DE815AD5-2889-E911-A3FF-FA163E03B91F.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/66AC7793-C987-E911-A87F-A4BF01158D70.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/00C7CE09-CF87-E911-BC3F-002590A80DF0.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/789E22DB-9F88-E911-8A03-001E677924B2.root',
'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/E47071D9-2789-E911-8665-A4BF0112BCF8.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/9CF894B4-6788-E911-B93D-0CC47A7FC72C.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/5C1037BA-7E88-E911-92AD-001B21ADD368.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/D8C9BD44-2889-E911-B62E-3417EBE706ED.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/E2D9E4D7-4187-E911-A08C-24BE05CEDCF1.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/78B96EF3-BC87-E911-8688-E0071B73B6F0.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/92F53C03-8888-E911-9E59-B8CA3A70A410.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/183E83F1-EE87-E911-B414-A4BF01013F8D.root',
#'/store/mc/RunIISummer16DR80Premix/SMS-T1qqqq-LLChipm_ctau-200_mLSP-1900_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_longlived_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/240000/DC5E7962-0288-E911-AD76-EC0D9A0B31B0.root',
] )












