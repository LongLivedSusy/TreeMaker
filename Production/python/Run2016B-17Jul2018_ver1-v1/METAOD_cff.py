import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/26ADD6D4-7798-E711-BE5D-A0369F83627A.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/A45E6893-CA98-E711-AE0C-7CD30ACDCCB0.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/544B3692-CA98-E711-ACE3-008CFAFBE6B2.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/F6123284-CD98-E711-AD78-7CD30AD09C64.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/60A3C11B-D498-E711-A1F6-008CFAFBE6E8.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/D8EEE619-D498-E711-805F-008CFAFC0416.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/F090931C-D498-E711-AA21-7CD30AD097C0.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/369CC01B-D498-E711-AF69-7CD30AB15C58.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/42999A49-D798-E711-B3DF-008CFAF7485E.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/40D0CB4C-D798-E711-9A2F-7845C4FC35CC.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/CCC42896-D898-E711-9616-008CFAFC043A.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/0460CA4F-D798-E711-9696-7845C4FC3C83.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/DA2889B4-D898-E711-856A-7845C4FC3782.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/3A865100-DF98-E711-83F1-7845C4FC359F.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/6ACB958B-E098-E711-B1E8-7845C4FC3C83.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/043DC26C-E598-E711-BADB-7CD30AD0A66C.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/D2B1C28D-E598-E711-BDB0-008CFAFBEBF2.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/AE480E66-E598-E711-AAAD-7CD30ACDC7B2.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/465E869E-EB98-E711-8E58-7CD30ACE2356.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/12BEE073-5899-E711-86C2-7CD30AD09B14.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/60AC674F-BF98-E711-858B-0025905C3DD6.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/562CC543-F298-E711-9489-0CC47AF9B1D6.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/F80FB354-2799-E711-9A89-0025904C66A2.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/682E46EE-3999-E711-B1A0-0025905C42A8.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/F0E97403-5399-E711-B498-0025904C669E.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/F89EE787-E098-E711-8489-0CC47A4DEF3A.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/4E6A1B76-B797-E711-9990-A4BF011255C0.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/3849488F-CA98-E711-8546-48FD8EE73A69.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/7EBCA980-CD98-E711-80A8-48FD8EE73A51.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/F2C5881D-D498-E711-A4BF-002590D0AF7C.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/966CF91B-D498-E711-AF87-48D539D33361.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/120D4215-0C99-E711-90F9-48D539D33357.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/B427B25B-CB98-E711-B736-0242AC11000D.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/D852B0B4-F298-E711-8FAA-0242AC110005.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/66CA8439-F898-E711-858D-0242AC110013.root',
'/store/data/Run2016B/MET/AOD/07Aug17_ver1-v1/110000/9CE1036C-5399-E711-B1DC-0242AC110004.root',
] )