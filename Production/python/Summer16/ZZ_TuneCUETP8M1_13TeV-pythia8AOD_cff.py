import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C0AF5058-4FD7-E611-BC14-008CFA5807F0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/94AF6F8F-52D7-E611-A522-549F358EB7E4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FCB2ED97-51D7-E611-95F8-008CFA1982C0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E0CBBC76-51D7-E611-A5B4-008CFA0A5684.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/583F1FFE-53D7-E611-9331-008CFA5807F0.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/382F16CE-58D7-E611-A51C-008CFA56D894.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/94FDF081-54D7-E611-B83A-008CFA110B10.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1A606BA5-55D7-E611-84E3-008CFA56D6F4.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/52CD2D6A-56D7-E611-9D13-549F358EB72E.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/441D2AF9-56D7-E611-8208-008CFA1982C0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/CA0AD96C-5CD7-E611-8972-008CFA151F98.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/0EDD6470-5CD7-E611-8DF3-008CFA1660F8.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A4D15917-5ED7-E611-9160-549F358EB72E.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/08BEE4EB-5DD7-E611-BE24-008CFA1C907C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/F4BC9ECB-60D7-E611-9567-A0369FC5E71C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/18894685-5FD7-E611-8F7F-549F35AD8BBC.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/04C426F8-62D7-E611-B481-A0369FD8FDB0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1C73D962-65D7-E611-8D16-A0369F7FC540.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/FC160ED2-60D7-E611-94F5-549F35AC7E56.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/E4D8F529-63D7-E611-9EBE-549F358EB72E.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/7ABB8D39-61D7-E611-AB7F-008CFA56D6F4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DEFDA50E-64D7-E611-93D8-549F35AE4F61.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BEEF98C1-5FD7-E611-BC8D-008CFA0A56F0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/C29F8F27-63D7-E611-9C24-008CFA0A5818.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/1AB357D4-5FD7-E611-9262-008CFA0A56F0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/BCE737CF-67D7-E611-9B48-008CFA111200.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A43D5A95-69D7-E611-B3EE-549F358EB72E.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/908D84FE-62D7-E611-930E-008CFA166008.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DED037E5-64D7-E611-BC0F-008CFA1982C0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/EED04E53-61D7-E611-B63F-008CFA197D2C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/DCFEE1D3-63D7-E611-B252-008CFA1C907C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/A07C042E-64D7-E611-A77E-008CFA0F51EC.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/72BF9405-65D7-E611-9579-008CFA1C907C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/3E2B282F-61D7-E611-9553-008CFA1C64B0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/80000/928BF9EA-88D7-E611-8B5E-008CFA1C645C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/BCE69B1E-A1D7-E611-9B1F-A0369F7FC524.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/24A09B2A-A1D7-E611-A76E-A0369F7F92E8.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/668CE921-A1D7-E611-92F1-008CFA56D6F4.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/4E79DE2D-B7D7-E611-9A9C-A0369FC5B438.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D4B863B2-BAD7-E611-AFF9-00266CFBE88C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/22D98384-BED7-E611-B6FD-549F35AE5024.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7AEFB3B9-BDD7-E611-8A48-008CFA1C64A0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D8BA5398-C0D7-E611-A45D-A0369F7F8E80.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3028C86D-BBD7-E611-88A2-00266CFCCB8C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F6614EB2-C3D7-E611-B1CD-A0369FC5F5A8.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5C7ED0A5-C1D7-E611-85FE-549F35AD8B6E.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/307F4247-C5D7-E611-AEAF-00266CFCC8D0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0A3D4164-D0D7-E611-9243-A0369F7F9170.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7A6D54BF-CBD7-E611-A115-008CFA197D98.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C0E93E11-CDD7-E611-91D8-008CFA56D770.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3AD77354-CFD7-E611-AC23-A0369F7FBF74.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/68243C03-D3D7-E611-A51B-A0369F7F9170.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/D4FA9404-D2D7-E611-B7A1-008CFA56D894.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/36C77A1B-D4D7-E611-9C4F-A0369FC5E090.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0E0F1B52-D3D7-E611-9B7D-A0369F7FBF74.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B0BEE5F1-D5D7-E611-B194-A0369FC5EBB0.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/88321A48-D7D7-E611-99FC-A0369F7F9170.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/EA7090F1-D5D7-E611-8B0F-549F35AD8B7B.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/3822CFF4-D5D7-E611-BDC5-008CFA0A5830.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A497F20D-D6D7-E611-8490-549F35AC7DFB.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/841580D2-DAD7-E611-A409-A0369F7FCB94.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B2B3BFC6-DAD7-E611-9695-A0369FC5EB28.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/806C588B-D8D7-E611-AD78-549F358EB7A3.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/5C5AD490-D8D7-E611-9F1D-549F358EB7A3.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C2642435-DDD7-E611-8437-A0369FC5D904.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/B044DE5D-DCD7-E611-98CC-A0369FC5F14C.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/98FE3239-DDD7-E611-AE08-A0369FC5D8F0.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A265EB96-D8D7-E611-9CB8-008CFA151F98.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/22855C9A-D8D7-E611-9865-008CFA56D894.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/DC766F95-D8D7-E611-86D7-008CFA151F98.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/C2526BE4-DAD7-E611-8715-008CFA05EA2C.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8CD37254-D7D7-E611-8230-008CFA0648E0.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/44CA1D3B-DDD7-E611-9621-008CFA56D770.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/8E49EE22-DED7-E611-8B91-549F35AD8B7B.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/34BC9653-E2D7-E611-BB56-008CFA56D894.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/06676257-D7D7-E611-B8F0-00266CFCC804.root',
'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/862E9F55-DCD7-E611-88F1-008CFA064878.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/F2EEE866-DCD7-E611-B119-008CFA064878.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/7805DDAB-DED7-E611-BCD6-549F35AC7DFB.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/9E622C70-DED7-E611-ACE7-008CFA0A5830.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/A4EFEC3B-DDD7-E611-9FD5-00266CF3DF00.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/AC9CC23D-DDD7-E611-B385-00266CFCC21C.root',
] )





















