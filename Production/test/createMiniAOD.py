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
