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

# check for incorrect pilot cert
vomsident = $(voms-proxy-info -identity)
echo $vomsident
if [[ $vomsident = *"cmsgli"* ]]; then
	# this is the exit code for "User is not authorized to write to destination site."
	rm *.root
	echo "exit code 60322, skipping file copy"	
	exit 60322
fi

cp "$CMSSW_BASE/src/TreeMaker/Production/test/file_loop.py" .
chmod +x file_loop.py
./file_loop.py --outpath=$OUTDIR --arguments="$ARGS"
CMSSWSTATUS=$?
if [[ $CMSSWSTATUS -ne 0 ]]; then
    echo "error $CMSSWSTATUS"
    exit CMSSWSTATUS
fi

rm *.root

