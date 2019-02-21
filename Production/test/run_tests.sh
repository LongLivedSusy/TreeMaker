#!/bin/bash

# let's test all data scenarios with miniAOD re-creation for TreeMaker

echo "test Run2016C rereco"
rm miniaod.root
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2016MiniAODv3AOD inputFilesConfig=Run2016C-17Jul2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
./createMiniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2016MiniAODv3AOD inputFilesConfig=Run2016C-17Jul2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi
# result: OK, Feb 21 commit cb9202e3420592bd31bd086e5d30586900c142c9

echo "test Run2016G rereco"
rm miniaod.root
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2016MiniAODv3AOD inputFilesConfig=Run2016G-17Jul2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
./createMiniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2016MiniAODv3AOD inputFilesConfig=Run2016G-17Jul2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi
# result: OK, Feb 21 commit cb9202e3420592bd31bd086e5d30586900c142c9

echo "test Run2017 rereco"
rm miniaod.root
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2017ReReco31MarAOD inputFilesConfig=Run2017C-31Mar2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
./createMiniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2017ReReco31MarAOD inputFilesConfig=Run2017C-31Mar2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi
# result: OK, Feb 21 commit cb9202e3420592bd31bd086e5d30586900c142c9

echo "test Run2018 rereco"
rm miniaod.root
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2018ReReco17Sep inputFilesConfig=Run2018A-17Sep2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
./createMiniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2018ReReco17Sep inputFilesConfig=Run2018A-17Sep2018-v1.METAOD nstart=0 nfiles=1 outfile=test numevents=10
if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi
# result: OK, Feb 21 commit 72b5e12106004451be296aa042e3bd68f96516a1

echo "test Run2018 prompt"
rm miniaod.root
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2018PromptRecoAOD inputFilesConfig=Run2018D-PromptReco-v2.METAOD nstart=0 nfiles=1 outfile=test numevents=10
./createMiniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"
cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=2018PromptRecoAOD inputFilesConfig=Run2018D-PromptReco-v2.METAOD nstart=0 nfiles=1 outfile=test numevents=10
if [[ $? -ne 0 ]]; then echo "Failed test"; else echo "Success"; fi
# result: OK, Feb 21 commit 72b5e12106004451be296aa042e3bd68f96516a1

