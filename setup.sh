#!/bin/bash -e

CMSSWVER=CMSSW_9_4_11
FORK=LongLivedSusy
BRANCH=Run2_2017_autominiaod
ACCESS=ssh
CORES=8
NAME=""
DIR="${PWD}"

usage(){
	EXIT=$1

	echo "setup.sh [options]"
	echo ""
	echo "-f [fork]           clone from specified fork (default = ${FORK})"
	echo "-b [branch]         clone specified branch (default = ${BRANCH})"
	echo "-c [version]        use specified CMSSW version (default = ${CMSSWVER})"
	echo "-a [protocol]       use protocol to clone (default = ${ACCESS}, alternative = https)"
	echo "-j [cores]          run CMSSW compilation on # cores (default = ${CORES})"
	echo "-n [name]           name of the CMSSW directory (default = ${CMSSWVER})"
	echo "-d [dir]            project installation area for the CMSSW directory (default = ${DIR})"
	echo "-h                  display this message and exit"

	exit $EXIT
}

# process options
while getopts "f:b:a:j:n:d:c:h" opt; do
	case "$opt" in
	f) FORK=$OPTARG
	;;
	b) BRANCH=$OPTARG
	;;
	c) CMSSWVER=$OPTARG
	;;
	a) ACCESS=$OPTARG
	;;
	j) CORES=$OPTARG
	;;
	n) NAME=$OPTARG
	;;
	d) DIR=$OPTARG
	;;
	h) usage 0
	;;
	esac
done

# check options
if [ "$ACCESS" = "ssh" ]; then
	ACCESS_GITHUB=git@github.com:
	ACCESS_GITLAB=ssh://git@gitlab.cern.ch:7999/
elif [ "$ACCESS" = "https" ]; then
	ACCESS_GITHUB=https://github.com/
	ACCESS_GITLAB=https://gitlab.cern.ch/
else
	usage 1
fi

# get CMSSW release
if [[ "$CMSSWVER" == "CMSSW_9_4_"* ]]; then
	GCC_VERSION=gcc630
elif [[ "$CMSSWVER" == "CMSSW_10_2_"* ]]; then
	GCC_VERSION=gcc700
else
	echo "Unsupported CMSSW version: $CMSSWVER"
	exit 1
fi

if [[ `uname -r` == *"el6"* ]]; then
	SLC_VERSION="slc6"
elif [[ `uname -r` == *"el7"* ]]; then
	SLC_VERSION="slc7"
else
	echo "WARNING::Unknown SLC version. Defaulting to SLC6."
	SLC_VERSION="slc6"
fi
export SCRAM_ARCH=${SLC_VERSION}_amd64_${GCC_VERSION}

# cmsrel
SCRAM_PROJECT_OPTIONS=""
if [ "$DIR" != "${PWD}" ]; then
	SCRAM_PROJECT_OPTIONS="$SCRAM_PROJECT_OPTIONS --dir ${DIR}"
fi
if [ "$NAME" != "" ]; then
	SCRAM_PROJECT_OPTIONS="$SCRAM_PROJECT_OPTIONS --name ${NAME}"
else
	NAME=${CMSSWVER}
fi
SCRAM_PROJECT_OPTIONS="$SCRAM_PROJECT_OPTIONS ${CMSSWVER}"
scram project ${SCRAM_PROJECT_OPTIONS}
cd ${DIR}/${NAME}/src

# cmsenv
eval `scramv1 runtime -sh`
git cms-init
git config gc.auto 0

# CMSSW patches
if [[ "$CMSSWVER" == "CMSSW_9_4_"* ]]; then
	git cms-merge-topic TreeMaker:fixFormulaEvaluator_949 # this one has dependencies, might be in a future 9_4_X release
	git cms-merge-topic -u TreeMaker:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_9_4_2
	git cms-merge-topic -u TreeMaker:storeJERFactorIndex942
	git cms-merge-topic -u TreeMaker:AddJetAxis1_942
	git cms-merge-topic -u TreeMaker:NjettinessAxis_948
	git cms-merge-topic -u TreeMaker:METFixEE2017_949_v2
elif [[ "$CMSSWVER" == "CMSSW_10_2_"* ]]; then
	git cms-merge-topic -u TreeMaker:BoostedDoubleSVTaggerV4-WithWeightFiles-v1_from-CMSSW_10_2_7
	git cms-merge-topic -u TreeMaker:storeJERFactorIndex1027
	git cms-merge-topic -u TreeMaker:AddJetAxis1_1027
	git cms-merge-topic -u TreeMaker:NjettinessAxis_1027
fi

# outside repositories
git clone ${ACCESS_GITHUB}TreeMaker/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_94X
git clone ${ACCESS_GITHUB}kpedro88/CondorProduction.git Condor/Production
git clone ${ACCESS_GITHUB}${FORK}/TreeMaker.git -b ${BRANCH}
# get egamma config file without recompiling whole package
wget https://github.com/TreeMaker/cmssw/raw/EgammaPostRecoTools_940/RecoEgamma/EgammaTools/python/EgammaPostRecoTools.py -P TreeMaker/Utils/python/

# compile
scram b -j ${CORES}

# extra setup
cd TreeMaker/Production/test/condorSub/
python $CMSSW_BASE/src/Condor/Production/python/linkScripts.py
