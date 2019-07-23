import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/1CD5D2D2-E38C-E711-93CC-008CFA1C64A0.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/8022623B-C48A-E711-9295-6C3BE5B58198.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/146A8318-028C-E711-9581-484D7E8DF092.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/BAEB9B14-028C-E711-8777-44A842CF058B.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/8E0F141D-028C-E711-BB79-001CC4C0B0DC.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/E0D52127-048C-E711-AF69-44A842CF05A5.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/B6A10B9F-058C-E711-B542-484D7E8DF051.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/1A409A9F-058C-E711-9629-44A842CF058B.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/8C94B38B-078C-E711-99F2-44A842CFD5F2.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/8611708F-078C-E711-8027-001CC4A64C3E.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/1052EE30-048C-E711-B49A-6C3BE5B5B340.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/1A944637-048C-E711-B67E-B499BAAB50A0.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/E06E35AB-058C-E711-98EE-6C3BE5B533A8.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/8283F7AA-058C-E711-9FDD-6C3BE5B533A8.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/74BD8099-078C-E711-853C-B499BAAB50A0.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/B8710237-048C-E711-9E9C-B499BAAC0572.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/10C98A90-098C-E711-871E-6C3BE5B593F8.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/92CE51FA-0A8C-E711-BC18-6C3BE5B533A8.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/DADA9394-078C-E711-A6C9-001F29087074.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/04769794-078C-E711-B6F3-001F29087074.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/B0795A89-098C-E711-BB11-001F29085CDE.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/A27D15FF-0A8C-E711-88AB-6C3BE5B59218.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/DC38291C-0D8C-E711-94B7-B499BAAC0658.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/383AAD3C-158C-E711-9280-484D7E8DF05E.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/240D4C13-138C-E711-8B0B-6C3BE5B5F228.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/362EF85C-1C8C-E711-9738-484D7E8DF0ED.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/E0BAA539-1A8C-E711-998F-6C3BE5B5F228.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/800FA447-1E8C-E711-8E91-44A842CF05B2.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/0A562ABF-228C-E711-AF43-44A842CFD619.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/826C1DC0-228C-E711-81A4-484D7E8DF05E.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/BC3BD0C7-228C-E711-A2D5-6C3BE5B5F228.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/84D0FD51-228C-E711-A4C8-484D7E8DF078.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/1A7853F4-238C-E711-95F3-44A842CFC971.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/1275D2EE-238C-E711-BE59-44A842CF05A5.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/16D5C903-228C-E711-B525-44A842CF05B2.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/22E9795B-228C-E711-B39C-001F2908CE58.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/E68C575B-288C-E711-A6A3-484D7E8DF09F.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/7C0685D3-228C-E711-8F49-D8D385B0EE2E.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/EAD3A7EA-258C-E711-AE79-44A842CFC9A5.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/02216D5B-268C-E711-A184-44A842CF05E6.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/6CCAFEF2-258C-E711-9B2F-001F2908CE36.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/46B8C6EF-258C-E711-89DE-001CC47D5894.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/00AA482A-2C8C-E711-8135-484D7E8DF0C6.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/202ECEF7-2F8C-E711-A1FD-44A842CF0600.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/E23CA876-3D8C-E711-B836-44A842CF05B2.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/5050066B-E88A-E711-A845-008CFA0A5818.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/E016C521-D68A-E711-8758-008CFA56D58C.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/B8AE39A5-D28A-E711-8A8B-008CFA0A59C0.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/62B0D9CC-E68A-E711-8EDD-008CFA0A570C.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/2A6FC9F0-EC8A-E711-8768-549F35AE4FC9.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/B0B7D728-F68A-E711-90DE-A0369F7FC210.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/120A97CF-F98A-E711-B6D9-549F35AE4FE3.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/327EC753-FC8A-E711-B049-008CFA56D764.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/A867EDC9-058B-E711-A912-008CFA56D764.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/24AB24A1-0A8B-E711-9DE4-008CFA0A59C0.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/30FF7B1D-0E8B-E711-A4CC-008CFA198258.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/7A0E7198-128B-E711-8633-A0369FC5B438.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/049800A0-128B-E711-A7CC-549F35AE4F61.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/9AEA388D-2C8B-E711-B502-008CFA56D794.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/CC6615EC-2E8B-E711-BC37-008CFA0A58B0.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/2220FCDC-388B-E711-A6CC-549F35AF44A2.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/AE14CDEE-4D8B-E711-B4E2-A0369FC5DCBC.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/68FDFA36-6C8B-E711-BE4A-549F35AE4FFD.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/08DE6604-8A8B-E711-BE79-008CFA0A58B4.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/BE06CC1C-A68B-E711-B60F-A0369F7FC2F8.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/7050D90D-B68B-E711-8FBB-008CFA1983E0.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/060D881A-028C-E711-BD89-008CFA197D38.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/A6921418-028C-E711-A9E6-549F358EB73B.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/C2279327-048C-E711-AE62-A0369FC51BB4.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/92E3719D-058C-E711-AEA8-A0369FC5E8FC.root',
#'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/E47D1DA1-058C-E711-9CBE-549F35AD8BFD.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/C291A5EF-0A8C-E711-BAAD-A0369FC5E530.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/CE18C8A3-058C-E711-AD64-008CFA56D794.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/04D8638C-098C-E711-9F4E-008CFA56D794.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/4C2A488D-078C-E711-9686-008CFA1983BC.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/04A2FB12-0D8C-E711-A420-549F35AC7E08.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/B0255DAF-118C-E711-A177-008CFA1C64A0.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/30CFFEA3-158C-E711-8E2E-A0369FC5F5A8.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/D4177F95-168C-E711-B48F-A0369F7FC6EC.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/7221F39C-168C-E711-805D-549F35AC7E7D.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/EA000E90-1A8C-E711-BE37-008CFA197D98.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/BE9E9B90-1A8C-E711-BA0A-008CFA197D98.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/180922D1-208C-E711-9C1E-A0369FC5E9A4.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/E2F5991D-238C-E711-98D7-A0369FC5B56C.root',
'/store/data/Run2016B/SingleElectron/AOD/07Aug17_ver1-v1/110000/F49B08C9-288C-E711-A16E-008CFA197EB0.root',
] )



















