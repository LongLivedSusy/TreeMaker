import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/159/00000/1E5A2F7F-D16B-E511-9AC0-02163E0135AC.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/159/00000/6E07CD15-D26B-E511-8668-02163E013999.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/174/00000/6E54FF23-A86C-E511-8BD3-02163E011D5C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/175/00000/4A8229C0-276D-E511-931E-02163E013870.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/177/00000/1A354274-416D-E511-BCF8-02163E0138B3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/177/00000/20CCCE6D-416D-E511-BC84-02163E0143B7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/177/00000/22C20D78-416D-E511-A443-02163E011B48.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/177/00000/3C806F61-416D-E511-81CB-02163E01432F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/177/00000/3E93CBC2-416D-E511-895F-02163E0142CD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/177/00000/72750D70-416D-E511-906E-02163E0141B6.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/177/00000/D6A54A99-416D-E511-AAF7-02163E01476B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/177/00000/EA26416D-416D-E511-862B-02163E014241.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/195/00000/920C782D-866C-E511-B233-02163E0138B3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/211/00000/942FDE7A-A86C-E511-8E76-02163E0138CE.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/213/00000/CCEAD4D7-426D-E511-84C2-02163E01432F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/214/00000/F86F9003-286D-E511-9164-02163E011AD7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/215/00000/00FCD95D-FA6C-E511-9577-02163E0137E3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/287/00000/D8E0EA7A-7D6D-E511-8ADE-02163E01464A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/312/00000/86F5D6BA-7A6D-E511-A4A7-02163E01375C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/313/00000/B008DDAE-DE6D-E511-ABFB-02163E011856.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/313/00000/D0CE32E1-DE6D-E511-A746-02163E01427E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/320/00000/124A2E7A-CE6D-E511-AE9E-02163E0125D4.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/320/00000/12C3FB83-CE6D-E511-9116-02163E014752.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/335/00000/48AB6181-CF6D-E511-905B-02163E01398A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/403/00000/8A974AAF-076E-E511-95D4-02163E011D8D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/423/00000/00E1E44D-286E-E511-94FC-02163E014287.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/425/00000/FEBCC225-3E6E-E511-ACAE-02163E0145A8.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/426/00000/FA6952B8-136E-E511-85A1-02163E0146A5.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/427/00000/2E9F58DE-326E-E511-9BF3-02163E013409.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/428/00000/22E4D472-ED6E-E511-85B3-02163E0134FA.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/428/00000/408C01AB-E56E-E511-B57B-02163E011941.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/432/00000/C08CBEFD-326E-E511-876F-02163E0141E2.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/434/00000/6AFF714A-666E-E511-977D-02163E012A7F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/434/00000/B8A83986-666E-E511-A003-02163E014473.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/440/00000/808142E1-986E-E511-9AD4-02163E01473E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/440/00000/BACC7AD3-986E-E511-AF7B-02163E013450.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/440/00000/FA2E15D3-986E-E511-B046-02163E01388D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/443/00000/DE0A5D46-D26E-E511-9DC0-02163E01348A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/444/00000/A019EF3C-D86E-E511-8348-02163E01383C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/445/00000/86B617A7-E56E-E511-94D8-02163E0119F1.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/446/00000/567977FA-E56E-E511-A1A5-02163E01268A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/448/00000/4492B766-0A6F-E511-B042-02163E0146ED.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/448/00000/546C0F66-0A6F-E511-B1AD-02163E0146ED.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/480/00000/384BB31A-F46E-E511-82B5-02163E012447.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/482/00000/E8720CB2-F46E-E511-AC25-02163E0133A0.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/486/00000/34CC7934-F66E-E511-A339-02163E01353F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/616/00000/F6B6FE50-846F-E511-86E0-02163E013647.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/655/00000/C2F400E1-2370-E511-B131-02163E013597.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/656/00000/34D29B0F-D870-E511-A0B2-02163E0146F3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/656/00000/C2B5462A-D870-E511-B4DD-02163E0120E3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/682/00000/56A899FE-4370-E511-B6A4-02163E01360B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/692/00000/488BD669-5370-E511-9F9A-02163E0141DF.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/694/00000/4E15C345-A570-E511-BC50-02163E011FE1.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/694/00000/804ADD46-A570-E511-90C8-02163E012310.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/702/00000/48EA22CA-2D71-E511-9496-02163E011982.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/702/00000/4A088CDC-2D71-E511-8804-02163E0145C5.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/702/00000/BCF7DAD1-2D71-E511-B8DE-02163E0142E6.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/703/00000/1E701B65-E371-E511-80BB-02163E0120E4.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/703/00000/C41E9A3C-E371-E511-8C75-02163E014650.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/703/00000/D852EA8A-E371-E511-8181-02163E014789.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/705/00000/7686E628-1E71-E511-B1AD-02163E01229D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/706/00000/764AF18A-A671-E511-9BAB-02163E01424F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/706/00000/9CD0E049-A671-E511-9E46-02163E0117FF.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/706/00000/A2A7A97B-A671-E511-8C70-02163E014292.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/706/00000/F0D6B8C1-A671-E511-A1D0-02163E013680.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/712/00000/8E68BA80-A771-E511-97FC-02163E0136E3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/712/00000/E469FC78-A771-E511-8FF9-02163E013912.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/713/00000/6A998F8B-8D71-E511-8233-02163E013598.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/714/00000/D0EEA09B-8D71-E511-9227-02163E0144BB.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/741/00000/586E0A36-FA71-E511-B8C5-02163E011A6A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/742/00000/48706B39-2B72-E511-9790-02163E013710.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/742/00000/4C849434-2B72-E511-9FB5-02163E0123B8.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/742/00000/72602F29-2B72-E511-A2DD-02163E0136E3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/742/00000/983AA02B-2B72-E511-B3EA-02163E013668.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/742/00000/C0BC6F34-2B72-E511-9372-02163E013686.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/745/00000/903C34C8-7372-E511-ADD3-02163E014685.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/745/00000/AE53D9E8-7372-E511-BCF1-02163E0146F8.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/749/00000/3684F02A-6272-E511-B0AD-02163E014193.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/749/00000/968EA6A6-6172-E511-AFBC-02163E012360.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/749/00000/F095AA96-6172-E511-AC88-02163E01455F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/750/00000/5EE58B11-7572-E511-B952-02163E014378.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/258/959/00000/7C9C1206-6F73-E511-8DC6-02163E0134A3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/458/00000/684893F4-5D78-E511-8903-02163E0146CD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/464/00000/1A21448D-8E78-E511-B62C-02163E01473F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/478/00000/C6072224-A177-E511-8E8E-02163E014316.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/626/00000/5A61310A-9D7A-E511-951B-02163E0143C8.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/636/00000/229A7EFB-4E7A-E511-ADEB-02163E0127EE.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/636/00000/C29BC008-4F7A-E511-A433-02163E0134B1.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/637/00000/D84890A2-F678-E511-A3FF-02163E0142B0.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/681/00000/94E70CFB-5779-E511-910B-02163E013391.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/682/00000/A48B0919-3979-E511-82B7-02163E01434A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/683/00000/0643E18B-247A-E511-BC36-02163E011EA7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/685/00000/28265767-097B-E511-B446-02163E014275.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/685/00000/BAE4CF61-097B-E511-89EA-02163E0146CD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/685/00000/D2C93270-097B-E511-8EBE-02163E01374E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/685/00000/F6E55C5B-097B-E511-A40A-02163E0123E9.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/686/00000/08CF7AC4-9B7A-E511-82AB-02163E014315.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/686/00000/5A302FCB-9B7A-E511-82A8-02163E0146C4.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/714/00000/4AA3B37F-E779-E511-9DFF-02163E01454F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/721/00000/16F8A4AF-9A7A-E511-8E54-02163E0144EF.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/809/00000/1E2DCF70-0D7B-E511-9787-02163E014447.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/809/00000/708D7B7B-0D7B-E511-9856-02163E0121DC.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/810/00000/DC35E3E2-297B-E511-B0E5-02163E011E2B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/811/00000/101A678F-187B-E511-9B0B-02163E011A52.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/812/00000/061999B1-387B-E511-970D-02163E011955.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/813/00000/A0DB599F-377B-E511-8AD0-02163E01398B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/817/00000/3C0C3A07-377B-E511-A7E0-02163E01378F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/818/00000/CC2F7A18-377B-E511-B0C7-02163E01419A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/820/00000/5C0FEEDD-977B-E511-9900-02163E014553.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/821/00000/4864D9BF-A77B-E511-8B61-02163E014485.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/822/00000/4471C0DE-9D7B-E511-91D5-02163E013779.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/822/00000/DC0428DD-9D7B-E511-BAE6-02163E014609.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/857/00000/E4447669-857B-E511-B1A1-02163E0142F5.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/861/00000/FEDCA3E7-2E7E-E511-91CD-02163E0142F5.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/862/00000/28AE2E5C-FA7B-E511-B43C-02163E0141C4.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/862/00000/60BD7F6E-FA7B-E511-B62F-02163E0140E7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/862/00000/C6D1145A-FA7B-E511-A413-02163E011AD3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/884/00000/D2C787C9-547E-E511-8BEB-02163E01185E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/890/00000/BEC29B4C-747C-E511-98A5-02163E0142E3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/259/891/00000/18CE906F-927C-E511-B1FE-02163E014648.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/335/00000/82D001B3-4580-E511-AC7B-02163E014142.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/340/00000/AC461E6B-4480-E511-B766-02163E014444.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/344/00000/46A4A8D6-4280-E511-807F-02163E01420C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/347/00000/3467BDE8-4780-E511-9301-02163E014698.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/348/00000/0895161A-4380-E511-8887-02163E011DEA.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/351/00000/7260D806-6480-E511-AA8F-02163E014182.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/366/00000/C0978818-A480-E511-B271-02163E0145D5.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/373/00000/B24633AB-0B81-E511-B3BB-02163E014129.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/403/00000/22BD863E-E480-E511-9B95-02163E011A82.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/422/00000/049C4B11-B683-E511-87B1-02163E0133E2.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/423/00000/70D4B20B-BF83-E511-9AF7-02163E01260E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/424/00000/14416577-9583-E511-966D-02163E012A0C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/424/00000/C080E38A-9583-E511-BDCA-02163E0133ED.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/424/00000/C0930E7E-9683-E511-9B6F-02163E013871.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/424/00000/EAEA1A6F-9583-E511-B767-02163E014556.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/425/00000/0852AA21-8A81-E511-B56B-02163E0121F3.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/425/00000/5C942B0A-8A81-E511-A6AD-02163E014520.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/425/00000/6270B6A3-8D81-E511-A58D-02163E0133DA.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/426/00000/0C4769AA-8A81-E511-A6B0-02163E0136E8.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/426/00000/A00B5E9E-8A81-E511-8A38-02163E01439E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/426/00000/AA280E9F-8A81-E511-A850-02163E011E2A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/427/00000/74977EA9-2583-E511-BF79-02163E0119E7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/427/00000/805469AA-2583-E511-8C03-02163E01435A.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/431/00000/1038D029-B283-E511-BC95-02163E013858.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/431/00000/7C664E2A-B283-E511-8D15-02163E014628.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/433/00000/5880BD2F-2F83-E511-96EB-02163E012A9F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/439/00000/0A6D157B-6A83-E511-8777-02163E01446E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/510/00000/02AA4ED8-6783-E511-8BED-02163E0124F7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/527/00000/7008BAD1-D683-E511-9065-02163E0134AF.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/528/00000/A444A0D7-4D83-E511-8650-02163E013842.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/532/00000/1A347A34-5783-E511-A9E1-02163E014707.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/532/00000/647FCF3A-5783-E511-84F1-02163E014424.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/532/00000/BC08D63E-5783-E511-9DA1-02163E01215B.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/532/00000/F2991F2E-5783-E511-AFF5-02163E011977.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/533/00000/500CB719-AE83-E511-8578-02163E014259.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/534/00000/0AB94649-B583-E511-BB7E-02163E011F0D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/534/00000/3E0BA339-B583-E511-9A08-02163E013506.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/536/00000/9AA914AF-3883-E511-88E6-02163E0138D8.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/538/00000/02936DB5-9683-E511-9CEF-02163E01384E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/538/00000/4A41CAB7-9683-E511-8699-02163E014195.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/540/00000/C29F25E8-6183-E511-9378-02163E014242.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/541/00000/B29ED351-D883-E511-A730-02163E0119E7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/568/00000/423C6A68-C183-E511-94EE-02163E0146AD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/570/00000/AA347DDB-8083-E511-8CB1-02163E0126AD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/571/00000/46474E19-1483-E511-96E9-02163E0146EC.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/572/00000/4EDE9265-ED83-E511-8989-02163E012A0C.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/575/00000/2CC1B077-1F84-E511-AEA5-02163E01291F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/576/00000/6EACFA00-5B84-E511-9DF1-02163E014696.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/576/00000/707F23FE-5A84-E511-81F7-02163E013842.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/576/00000/8E311203-5B84-E511-9EE6-02163E01442F.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/576/00000/F22AE1F4-5A84-E511-AACD-02163E0135AD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/577/00000/D0282375-E583-E511-8EA1-02163E0142B7.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/583/00000/026E16C0-1C83-E511-A434-02163E0135AD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/593/00000/AC22D10E-0E84-E511-AFC0-02163E0142CD.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/593/00000/DC5D8706-0E84-E511-8D18-02163E014570.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/593/00000/E638C90C-0E84-E511-B377-02163E014383.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/0A9B28E8-E284-E511-9E94-02163E012317.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/164FCA03-E384-E511-9CC0-02163E014665.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/62ADE6D8-E284-E511-A0CA-02163E0135C8.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/62BACC03-E384-E511-AFCD-02163E014665.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/6C6F43E7-E284-E511-9964-02163E014349.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/6EBD4FE4-E384-E511-9E91-02163E01476D.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/70AB25E8-E284-E511-96C3-02163E012317.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/90DC90E5-E284-E511-A76A-02163E014713.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/96EBA7E1-E284-E511-B1BA-02163E011D48.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/CA6EE442-E384-E511-9DC5-02163E014760.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/627/00000/E0FDFD10-E384-E511-B673-02163E01432E.root',
       '/store/data/Run2015D/MET/MINIAOD/PromptReco-v4/000/260/727/00000/80D39387-C084-E511-83E1-02163E0146D9.root' ] );


secFiles.extend( [
               ] )
