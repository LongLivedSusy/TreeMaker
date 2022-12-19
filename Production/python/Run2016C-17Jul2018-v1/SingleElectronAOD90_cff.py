import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016C/SingleElectron/AOD/07Aug17-v1/70000/100D8F21-9487-E711-AF1A-001E674FBFC2.root',
       '/store/data/Run2016C/SingleElectron/AOD/07Aug17-v1/50000/1C833266-228A-E711-80F6-0CC47AA53D5A.root',
       '/store/data/Run2016C/SingleElectron/AOD/07Aug17-v1/110000/0814A957-5F86-E711-A26B-485B3919F0B9.root',
       '/store/data/Run2016C/SingleElectron/AOD/07Aug17-v1/110001/0276DE2B-7786-E711-BF27-C81F66B73FCE.root',
       '/store/data/Run2016C/SingleElectron/AOD/07Aug17-v1/50001/762986AE-F88A-E711-8469-0025905A6070.root',
       '/store/data/Run2016C/SingleElectron/AOD/07Aug17-v1/110000/E2AC024B-4586-E711-918A-0CC47AA98F92.root',
       '/store/data/Run2016C/SingleElectron/AOD/07Aug17-v1/50000/327FDC1B-3489-E711-899C-E0071B73C630.root',
       '/store/data/Run2016C/SingleElectron/AOD/07Aug17-v1/90000/6C143EE2-1C86-E711-A15E-001E67A401B3.root',
] )
