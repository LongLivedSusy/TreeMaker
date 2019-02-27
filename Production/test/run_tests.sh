#!/bin/bash

echo "test Run2016C rereco"
rm info_*
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2016MiniAODv3 inputFilesConfig=Run2016C-17Jul2018-v1.METAOD nstart=5 nfiles=1 outfile=test numevents=10
./get_miniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2016MiniAODv3 inputFilesConfig=Run2016C-17Jul2018-v1.METAOD nstart=5 nfiles=1 outfile=test numevents=10
if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi
# OK!

echo "test Run2017 rereco"
rm info_*
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2017ReReco31Mar inputFilesConfig=Run2017E-31Mar2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
./get_miniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2017ReReco31Mar inputFilesConfig=Run2017E-31Mar2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi
# OK! ret

echo "test Run2018 rereco"
rm info_*
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2018ReReco17Sep inputFilesConfig=Run2018A-17Sep2018-v1.METAOD nstart=0 nfiles=1 outfile=Run2018A-17Sep2018-v1.METAOD numevents=10
./get_miniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2018ReReco17Sep inputFilesConfig=Run2018A-17Sep2018-v1.METAOD nstart=0 nfiles=1 outfile=Run2018A-17Sep2018-v1.METAOD numevents=10
if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi
# OK! ret

echo "test Run2018 rereco"
rm info_*
cmsRun runMakeTreeFromMiniAOD_cfg.py outfile=Run2018B-17Sep2018-v1.SingleMuonAODTEST_2 inputFilesConfig=Run2018B-17Sep2018-v1.SingleMuonAOD nstart=2 nfiles=1 scenario=2018ReReco17Sep
./get_miniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"
cmsRun runMakeTreeFromMiniAOD_cfg.py outfile=Run2018B-17Sep2018-v1.SingleMuonAODTEST_2 inputFilesConfig=Run2018B-17Sep2018-v1.SingleMuonAOD nstart=2 nfiles=1 scenario=2018ReReco17Sep


echo "test Run2018 prompt"

if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi

echo "test Fall17 MC"

if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi

echo "test Summer16 MC"

if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi

