import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DE4B68EF-D5B0-E611-AB36-24BE05C668E1.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E258E7D1-DBB0-E611-88BD-24BE05C626B1.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/004CA99F-44B1-E611-9DF1-5065F381A251.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/BA701B7B-45B1-E611-AF3B-008CFA197C10.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A08D0A82-DEB0-E611-AD57-0CC47A7E0006.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E019C372-E1B0-E611-A15F-0025904B1370.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4095CFF5-E9B0-E611-9D45-0CC47A7FC7C8.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5A7DB1F3-E9B0-E611-B77F-0CC47A7FC44E.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CED296AA-F2B0-E611-801D-0CC47A78A468.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2810B927-F8B0-E611-879B-0CC47A74527A.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8237CA09-F7B0-E611-91D6-003048FFD7A4.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/802B766F-FDB0-E611-AD4C-0CC47A4D76D2.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/86C60F6B-FEB0-E611-AC2E-0CC47A4C8F1C.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8E8D5D5E-02B1-E611-B1FC-0025905B85E8.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/84EEE855-00B1-E611-B011-0CC47A78A4B8.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/24958C64-07B1-E611-A9A3-0CC47A7452DA.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/ECBE82F6-05B1-E611-B58B-0CC47A7C3458.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/82EDE802-06B1-E611-8E5C-0025905A60FE.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/802D886A-07B1-E611-AA6B-0CC47A4C8E20.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/30AD06D8-09B1-E611-BF41-0CC47A4C8E16.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FE70E1AF-0BB1-E611-A7DB-0CC47A745282.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/408CD4DF-0DB1-E611-B539-0CC47A74527A.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E8851D65-52B1-E611-B36F-0CC47A4D764A.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C8D7E966-52B1-E611-9B70-0025905A48C0.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A0DA114F-EFB0-E611-B19A-B083FECFF2BF.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2AFA5536-F7B0-E611-A0AE-549F3525C4EC.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/521610E3-FBB0-E611-A4BE-1866DAEA6CF0.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/881302CB-02B1-E611-B23A-842B2B180A9F.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0CDFFA64-07B1-E611-AB82-D4AE526DEBEC.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E87CEBEC-0AB1-E611-8BEE-14187741278B.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FA1DF64E-E1B0-E611-93FE-0CC47A4C8E66.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8E66785D-FBB0-E611-AAB7-0CC47A7C347E.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8A8DE7D6-44B1-E611-9159-0025905B8600.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8CF35A90-E7B0-E611-95B2-24BE05C4D821.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/90C0CA3E-EEB0-E611-9603-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/42A5EB55-F2B0-E611-8412-5065F382C261.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3C6CBE37-F5B0-E611-BB9C-5065F37D4131.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4E939C9A-F8B0-E611-90DB-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A838FDFB-FAB0-E611-AB62-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E456712F-FEB0-E611-9518-A0000420FE80.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4C850013-04B1-E611-857A-24BE05CE3EA1.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/64A55039-00B1-E611-BEF1-A0369F30FFD2.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2E30DF62-07B1-E611-9E8E-24BE05CEFDF1.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/285818B3-06B1-E611-BA19-24BE05C3CCE1.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/12A49267-06B1-E611-B876-A0369F30FFD2.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2ABF398D-51B1-E611-A086-A0000420FE80.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/1CD5EE31-FAB0-E611-B1AE-0025904A8592.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/24B4B387-52B1-E611-85EE-008CFA1974D8.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/827E87B2-EFB0-E611-A77D-002590D9D8BE.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/829ABA05-38B2-E611-AA94-02163E015D81.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/6C709675-36B2-E611-8E68-FA163E8DA59B.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/CA4AB898-36B2-E611-ADE0-FA163E58A6D6.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0A1323CA-E8B0-E611-B13C-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA9D8BD3-EAB0-E611-B269-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7CB5A1B5-ECB0-E611-A390-0242AC130003.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/30AE3BCB-EAB0-E611-9C8D-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/2A9B55B4-ECB0-E611-984C-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A0EB6F24-F1B0-E611-B26C-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6E454080-F2B0-E611-A55B-0242AC130008.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0CDFE427-F1B0-E611-AA1A-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/CA7D3071-F5B0-E611-BBE3-0242AC130008.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E818987B-F2B0-E611-B58B-0242AC130005.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6653E034-F7B0-E611-9AFF-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9EA35872-F5B0-E611-B00F-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F052D99B-F9B0-E611-AEB7-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/988A81DE-F7B0-E611-BFA8-0242AC130008.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3A57AA33-F7B0-E611-8F45-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B48F7FF5-F3B0-E611-8886-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8EB4A20A-F4B0-E611-93A1-001E674FB149.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/36F7E541-02B1-E611-9417-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C6E73DBE-F8B0-E611-ABB9-001E674FB149.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D6F15F97-FCB0-E611-A350-001E67586A2F.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/58CE286F-07B1-E611-A59A-0242AC130008.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3AF6B2FA-00B1-E611-915E-0CC47A537688.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D2B92FF6-09B1-E611-8193-0242AC130004.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/72044420-04B1-E611-9028-001E674FB149.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AE1EDB0A-FFB0-E611-A735-001E674DA83D.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E831D8F2-0DB1-E611-B307-0242AC130003.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3241E70F-01B1-E611-8D8D-001E674FB149.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3C35F9A3-52B1-E611-B656-0242AC130005.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A4FCFCDA-51B1-E611-8F64-001E67E6920C.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2A32A37F-A6B0-E611-A692-ECF4BBE16338.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8AAD7982-A6B0-E611-97BC-001E67456F68.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7496F3A6-A8B0-E611-BA28-001E67456F68.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/04F11512-AEB0-E611-8949-0242AC130008.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/240D62DA-ADB0-E611-B4F1-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7E8144A7-A8B0-E611-80E9-001E674FB207.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EA1E646E-AEB0-E611-9211-ECF4BBE1CA28.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F84C3806-BBB0-E611-9ABF-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/54589732-B4B0-E611-A674-001E67457E36.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A29F5905-B7B0-E611-9965-ECF4BBE1CA28.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/DC5EC7B9-BEB0-E611-9332-0242AC130008.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E888ADB4-B6B0-E611-92AD-001E674FB24D.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/228E144F-C6B0-E611-AE0E-0242AC130006.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/34C1215C-C6B0-E611-A7B2-0242AC130003.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/422A3E69-C1B0-E611-9A14-001E67586A2F.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D0FC3E9B-C4B0-E611-943B-001E674FB207.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B4386565-C8B0-E611-825F-ECF4BBE1CA28.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E09D29AD-D0B0-E611-AEEF-0242AC130003.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4633BB56-D1B0-E611-9C91-0242AC130003.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E442E278-D0B0-E611-ABB3-0242AC130003.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AC5E0541-D4B0-E611-B391-0242AC130008.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F82C69DA-C6B0-E611-9B99-001E674FB207.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/AE23942C-D4B0-E611-A799-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/44508503-CCB0-E611-900C-ECF4BBE1CF30.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8AA10F08-C9B0-E611-B307-001E674DA347.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/904DE081-D1B0-E611-ABCE-ECF4BBE1CA28.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/2E768F23-D8B0-E611-B3D3-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7E576082-D1B0-E611-961E-001E674FAF23.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D41F3B78-D8B0-E611-9696-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/B602720F-DCB0-E611-9512-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/94129099-D2B0-E611-BF62-001E674DA83D.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/28E5D7DB-E1B0-E611-97F2-0242AC130002.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/640F0F36-D6B0-E611-A539-001E67397CB5.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C031875A-DEB0-E611-A142-ECF4BBE1CA28.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7A6A79F3-DDB0-E611-A900-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/786ED34A-DAB0-E611-9FA4-001E674FB063.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/22A04859-DAB0-E611-87FF-001E674FB207.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/FAF94FF9-DDB0-E611-A3AE-001E674FB149.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D6F3EB71-DFB0-E611-943E-001E674DA1AD.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/16AD035B-EAB0-E611-9B8E-0242AC130005.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4AB51053-EAB0-E611-A137-ECF4BBE1CA28.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/68EDD9A0-E6B0-E611-AC2D-001E67397CB5.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A8EFCE56-EAB0-E611-8BC1-001E674FB149.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/987DCC53-EAB0-E611-A61A-001E674FB24D.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/06D54155-EAB0-E611-A512-001E674DA347.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/04F5A20A-F7B0-E611-A1A3-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A6C4B665-F3B0-E611-A31A-0CC47A546E5E.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/5A4AE501-F4B0-E611-93D9-D067E5F91B8A.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/4487EC60-20B1-E611-984F-0242AC130003.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8057CED0-1CB1-E611-91F1-001E674FAF23.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/E61E1C61-20B1-E611-A9DA-0242AC130004.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/F6B16BD0-27B1-E611-AE90-0242AC130004.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/7A7FBC00-19B1-E611-AF74-001E674DA83D.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/58DCE6C9-1CB1-E611-B6CA-001E67586A2F.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/80A060B3-2CB1-E611-8089-001E67586A2F.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D8921BEB-35B1-E611-84AB-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9A2B34C4-39B1-E611-9722-0242AC130004.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/9C73AA5B-32B1-E611-891F-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D42A4B9A-31B1-E611-B032-001E67457E7C.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/EA6EB655-38B1-E611-89BC-D067E5F92184.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/746CEFB5-35B1-E611-A5B3-001E674FAF23.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1AB9604F-38B1-E611-B2E6-D067E5FB77E0.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/18EA0B9A-45B1-E611-8ECB-0242AC130005.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/16D3178C-20B0-E611-B209-0242AC130005.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3647FC95-20B0-E611-9C59-0242AC130004.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/26573F5C-1CB0-E611-BF9D-ECF4BBE1C9D8.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/84E81E1D-1EB0-E611-BDC4-ECF4BBE1CA20.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/DE0B7537-1CB0-E611-AD4B-D067E5F914D3.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/68EFB236-1CB0-E611-BB1E-D067E5F914D3.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/52124B7B-1EB0-E611-A0DD-001E67457E36.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/FC72EB70-1EB0-E611-920C-ECF4BBE1CF30.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/064DAD7A-1EB0-E611-A70A-001E674FC800.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/F8864313-1EB0-E611-A3C6-ECF4BBE16148.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C0DC3201-1EB0-E611-8CF9-ECF4BBE1CF80.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/6C317E0A-1EB0-E611-9073-ECF4BBE16338.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4C0AB8EF-27B0-E611-9E38-0CC47A546E5E.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/7C88CE75-1EB0-E611-8515-001E674FB063.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/CCC5AA7A-1EB0-E611-B366-001E674FC800.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/C68BC018-1EB0-E611-B8D5-001E674FCA99.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/34D6CD7A-1EB0-E611-A089-001E674FC800.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/3E685B6C-26B0-E611-8AAF-001E674FAF23.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/524E0F75-29B0-E611-BC9B-ECF4BBE15B60.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5637086A-26B0-E611-8C0C-001E674FB149.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/00773A54-2AB0-E611-B9A2-001E674FB207.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/60F119CA-D1B0-E611-9C46-0242AC130002.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3EA88C4E-E1B0-E611-9315-3417EBE64444.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/82D43FF0-E9B0-E611-B9D4-848F69FD29D3.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/180344D1-44B1-E611-8F66-3417EBE643E7.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B40139CB-F2B0-E611-AF86-0CC47AA989CA.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7881B228-FBB0-E611-8D53-90B11C27EA38.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/86D5352B-04B1-E611-94B7-90B11C2AA388.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4E81064F-0AB1-E611-BB22-90B11C27F5F0.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6A4B7E25-08B1-E611-B44F-0CC47A13CEF4.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/6A794D19-53B1-E611-BF5A-0CC47AA989C4.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/1AF28D8C-44B1-E611-A161-C81F66B7EBF5.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/76666F0B-F6B0-E611-996B-02163E01653B.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/26486331-FAB0-E611-8087-FA163E4625E4.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/E4657043-FAB0-E611-82F8-FA163E689750.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/40FAD21B-01B1-E611-89B1-002590494DC0.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5AD130EC-09B1-E611-AE11-2C600CAFEDE4.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/24EE88EA-FEB0-E611-9F63-FA163EE7154E.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9A17F670-07B1-E611-8E5D-FA163E2730B1.root',
'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4E345448-51B1-E611-B9FA-FA163E23B7E0.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8694AA2C-51B1-E611-98E9-FA163E20F6DB.root',
#'/store/mc/RunIISummer16DR80Premix/WWTo2L2Nu_13TeV-powheg/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3EC0F8E3-44B1-E611-A88A-00266CFFC0C0.root',
] )






























