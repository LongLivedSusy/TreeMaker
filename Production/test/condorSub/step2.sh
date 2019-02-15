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

# if input is given in AOD, convert to miniAOD:
cmsDriver.py step3 --filein file:%s --fileout file:%s --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 100X_upgrade2018_realistic_v10 --step PAT --nThreads 1 --era Run2_2017 -n -1


# run CMSSW
ARGS=$(cat args_${JOBNAME}_${PROCESS}.txt)
if [[ -n "$REDIR" ]]; then
	ARGS="$ARGS redir=${REDIR}"
fi
THREADS=$(getFromClassAd RequestCpus)
if [[ -n "$THREADS" ]]; then
	ARGS="$ARGS threads=${THREADS}"
fi

# run cmsRun the first time to get input file name...
echo "cmsRun runMakeTreeFromMiniAOD_cfg.py ${ARGS} 2>&1"
cmsRun runMakeTreeFromMiniAOD_cfg.py ${ARGS} 2>&1

echo "
#!/bin/env python
import os
from optparse import OptionParser
import commands

# create miniAOD file from AOD file, e.g.:
# ./createMiniAOD.py --aodfile=root://cmsxrootd.fnal.gov//store/data/Run2018A/MET/AOD/17Sep2018-v1/120000/8B09BCD4-ACB4-D343-823F-9FFF2EC9472E.root

parser = OptionParser()
parser.add_option('--infile', dest='infile')
parser.add_option('--outfile', dest='outfile')
(options, args) = parser.parse_args()

print 'Creating miniAOD file for AOD:', options.infile

if not 'root://' in options.infile:
    options.infile = 'root://cmsxrootd.fnal.gov/' + options.infile

if '/data/' in options.infile:
    is_data = True
else:
    is_data = False

conditions = {
                '17Sep2018': ['CMSSW_10_2_4_patch1', '102X_dataRun2_Sep2018Rereco_v1', 'Run2_2018']
             }

for condition in conditions:
    if condition in options.infile:
        cmssw_version = conditions[condition][0]
        global_tag = conditions[condition][1]
        era = conditions[condition][2]

if is_data:
    command = 'cmsDriver.py miniAOD-prod -s PAT --eventcontent MINIAOD --runUnscheduled --data --conditions %s --era %s --filein %s --fileout file:%s -n -1' % (global_tag, era, options.infile, options.outfile)
else:
    command = 'cmsDriver.py miniAOD-prod -s PAT --eventcontent MINIAODSIM --runUnscheduled --mc --conditions %s --era %s --filein %s --fileout file:%s -n -1' % (global_tag, era, options.infile, options.outfile)

jobscript = '''#!/bin/zsh
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
cmsrel CMSBASE
cd CMSBASE/src
eval `scramv1 runtime -sh`
echo $CMSSW_BASE
cd -
COMMAND
'''

fjob = open('createMiniAOD.sh','w')
fjob.write(jobscript.replace('CMSBASE',cmssw_version).replace('COMMAND',command))
fjob.close()

status, text = commands.getstatusoutput('sh createMiniAOD.sh')

print 'Output:\n', status, text

exit(status)
" > createMiniAOD.py

echo "first need to create miniAOD file"
oldbase=$CMSSW_BASE
chmod +x createMiniAOD.py
./createMiniAOD.py --infile="$(cat aodfile)" --outfile=miniaod.root
echo "running again cmsRun..."

cd $oldbase
eval `scramv1 runtime -sh`
cd -

# run cmsRun the second time to run with miniaod.root in sidecar
cmsRun runMakeTreeFromMiniAOD_cfg.py ${ARGS} 2>&1
CMSEXIT=$?

rm runMakeTreeFromMiniAOD_cfg.py

if [[ $CMSEXIT -eq 77 ]]; then
  echo "file already processed"
  exit 0
fi

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

# write short test script to check if output file has track collection:
echo "
import os, sys, glob
from ROOT import *
output_filename = glob.glob('*.root')[0]
fin = TFile(output_filename, 'read')
tree = fin.Get('TreeMaker2/PreSelection')
if tree.GetBranch('tracks'):
    print 'File OK'
else:
    print 'no tracks collection, deleting output file'
    os.system('rm ' + output_filename)
    sys.exit(919191)
" > check.py
python check.py
if [[ $? -ne 0 ]]; then
	# this is the exit code for missing branch "tracks" in output file:
    exit 51919
fi

# copy output to eos
echo "gfal-copy output for condor"
if [ -e "/cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh" ]; then
    . /cvmfs/oasis.opensciencegrid.org/mis/osg-wn-client/3.3/current/el6-x86_64/setup.sh
fi
for FILE in *.root
do
  echo gfal-copy -n 1 "file:////$PWD/${FILE}" "${OUTDIR}${FILE}"
  gfal-copy -n 1 "file:////$PWD/${FILE}" "${OUTDIR}${FILE}"
  XRDEXIT=$?
  if [[ $XRDEXIT -ne 0 ]]; then
    rm *.root
    echo "exit code $XRDEXIT, failure in xrdcp"
    exit $XRDEXIT
  fi
  rm ${FILE}
done

