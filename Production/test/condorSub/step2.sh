#!/bin/bash

# check for incorrect pilot cert
vomsident=$(voms-proxy-info -identity)
echo $vomsident
if [[ $vomsident = *"cmsgli"* ]]; then
	# this is the exit code for "User is not authorized to write to destination site."
	exit 60322
fi

export JOBNAME=""
export PROCESS=""
export OUTDIR=""
export REDIR=""
export OPTIND=1
while [[ $OPTIND -lt $# ]]; do
	# getopts in silent mode, don't exit on errors
	getopts ":j:p:o:x:" opt || status=$?
	case "$opt" in
		j) export JOBNAME=$OPTARG
		;;
		p) export PROCESS=$OPTARG
		;;
		o) export OUTDIR=$OPTARG
		;;
		x) export REDIR=$OPTARG
		;;
		# keep going if getopts had an error
		\? | :) OPTIND=$((OPTIND+1))
		;;
	esac
done

echo "parameter set:"
echo "OUTDIR:     $OUTDIR"
echo "JOBNAME:    $JOBNAME"
echo "PROCESS:    $PROCESS"
echo "REDIR:      $REDIR"
echo ""

# link files from CMSSW dir
ln -s ${CMSSWVER}/src/TreeMaker/Production/test/data
ln -s ${CMSSWVER}/src/TreeMaker/Production/test/runMakeTreeFromMiniAOD_cfg.py

# run CMSSW
ARGS=$(cat args_${JOBNAME}_${PROCESS}.txt)
if [[ -n "$REDIR" ]]; then
	ARGS="$ARGS redir=${REDIR}"
fi
THREADS=$(getFromClassAd RequestCpus)
if [[ -n "$THREADS" ]]; then
	ARGS="$ARGS threads=${THREADS}"
fi

# run cmsRun the first time to get input & output file names and other information such as json file, number of events
echo "cmsRun runMakeTreeFromMiniAOD_cfg.py ${ARGS} 2>&1"
cmsRun runMakeTreeFromMiniAOD_cfg.py ${ARGS} 2>&1

echo "check if output file already exists:"
echo "xrdfs root://dcache-cms-xrootd.desy.de/ stat ${OUTDIR//srm:\/\/dcache-se-cms.desy.de}/$(cat info_outfilename).root"
xrdfs root://dcache-cms-xrootd.desy.de/ stat ${OUTDIR//srm:\/\/dcache-se-cms.desy.de}/$(cat info_outfilename).root
if [[ $? -eq 0 ]]; then
   echo "outfile file already exists on dcache, exiting"
   exit 0
fi

# locate the corresponding miniAODs... come to papa
cp "$CMSSW_VERSION/src/TreeMaker/Production/test/get_miniAOD.py" .
chmod +x get_miniAOD.py
./get_miniAOD.py --infile="$(cat info_aodfilename)" --outfile=miniaod.root --nev="$(cat info_nev)"

if [[ $? -eq 123 ]]; then
  echo "empty union json, ignoring lumisection"
  exit 0
fi


# run cmsRun the second time to run with miniaod.root in sidecar
cmsRun runMakeTreeFromMiniAOD_cfg.py ${ARGS} 2>&1
CMSEXIT=$?

rm runMakeTreeFromMiniAOD_cfg.py
rm miniaod.root

if [[ $CMSEXIT -ne 0 ]]; then
  rm *.root
  echo "exit code $CMSEXIT, skipping xrdcp"
  exit $CMSEXIT
fi

# check for incorrect pilot cert
vomsident = $(voms-proxy-info -identity)
echo $vomsident
if [[ $vomsident = *"cmsgli"* ]]; then
	# this is the exit code for "User is not authorized to write to destination site."
	rm *.root
	echo "exit code 60322, skipping xrdcp"	
	exit 60322
fi

# run test script to check if output file has a tracks collection:
cp "$CMSSW_VERSION/src/TreeMaker/Production/test/check_if_tracks_present.py" .
chmod +x check_if_tracks_present.py
python check_if_tracks_present.py
if [[ $? -ne 0 ]]; then
	# this is the exit code for missing branch "tracks" in output file:
    exit 519
fi

# copy output: prepare gfal tools
echo "gfal-copy output for condor"
if [ -e "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh" ]; then
    . /cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh
fi
for FILE in *.root
do

  # try up to 20 times with 100s sleep in between to copy the file to dcache

  XRDEXIT=0
  n=0
  until [ $n -ge 20 ]
  do
    echo gfal-copy -n 1 "file:////$PWD/${FILE}" "${OUTDIR}${FILE}"
    gfal-copy -n 1 "file:////$PWD/${FILE}" "${OUTDIR}${FILE}" && break
    XRDEXIT=$?
    n=$[$n+1]
    echo "gfal-copy failed, retrying in 100s"
    sleep 100
  done
 
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done

