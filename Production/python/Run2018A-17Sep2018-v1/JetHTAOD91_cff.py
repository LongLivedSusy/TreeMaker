import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/00001/B3FBBCCE-CE2C-3242-A834-EBD33866F2B3.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/110008/5DA85A41-5918-7A4F-BF13-BA7691993267.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/100001/F840CC02-FB4F-DB4C-908C-F516FBCBD7A5.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/60012/E8E584F5-E788-D942-84B0-D5D75FE2ABDC.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/60002/7EEAD88E-D475-7546-86C9-4375F75D68BA.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/60003/BA5C8B18-AFA4-7142-A630-7E369BF25A92.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/00000/3310AE1C-DEA5-F640-AAAA-B091D66F3B23.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/270006/9BFDB25D-0B4F-AB48-809F-2A23C293AB91.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/60003/CE167B11-71C5-AA40-B967-36863A3865C1.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/270000/B91EA9B8-1DDB-CD44-BE1A-29884ACA01C6.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/60002/9AC16BA0-DA50-C242-B229-7D85315A65C1.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/60003/CCE3677D-060A-EA4D-BA64-22BEE9991079.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/00001/888990E7-87A3-F646-8736-6B5ED3A5696F.root',
       '/store/data/Run2018A/JetHT/AOD/17Sep2018-v1/60012/1F664CDA-A7D5-DC4F-A620-4ACF1861B4A4.root',
] )
