import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source("PoolSource", fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/70000/D682D614-188D-E711-A47A-48FD8E282489.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/110000/EAF2E706-878C-E711-B70A-20CF3019DEF2.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/50000/4EA381D3-AF93-E711-8FF2-0025905C5488.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/50000/6A648341-B893-E711-B840-0025904C66EC.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/110000/C04B8996-7796-E711-9335-0242AC11000B.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/50001/E85877E4-8A99-E711-8AA3-02163E01A5BF.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/10001/B80537D9-9C92-E711-B663-D48564594FB4.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/10000/086563AC-7A92-E711-9101-0CC47A1DF800.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/70000/5026F516-A193-E711-A679-0242AC11000A.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/70000/823DA827-C693-E711-996B-0025905C2C84.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/70000/743BD737-A193-E711-AD95-0025905C3DCE.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/70000/D80A95F4-9893-E711-A74F-0025905BA734.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/70000/743BD737-A193-E711-AD95-0025905C3DCE.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/70000/823DA827-C693-E711-996B-0025905C2C84.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/50000/AAB7A499-EE8C-E711-B0D3-002590D4FC42.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/10000/4E5ADEA8-B48C-E711-A587-3417EBE64405.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/10000/085DAB18-C08C-E711-AB53-002590D60036.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/50000/305C5514-ED92-E711-A9FE-0242AC110009.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/10001/083AD7FA-F692-E711-81E3-002590E7DEBE.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/110000/185609CD-AB94-E711-A43F-008CFAFBF618.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/70000/E874D882-0D8D-E711-904D-0242AC110005.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/10000/0AAAFD21-528C-E711-94A6-0CC47A1DF620.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/110000/78117379-D593-E711-8197-00259073E51E.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/50000/5458B2CB-DA93-E711-BDDA-0025905C54F4.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/110000/DA6E88AE-A08C-E711-8D9B-F04DA274E02A.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/70000/DE64EE7A-4093-E711-B11F-1418776375C9.root',
#       '/store/data/Run2016F/SingleElectron/AOD/07Aug17-v1/50000/8AE99F4C-E88C-E711-B079-0090FAA1ACF4.root',
] )
