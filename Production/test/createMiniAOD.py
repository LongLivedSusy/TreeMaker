#!/bin/env python
import os
from optparse import OptionParser
import commands

# create miniAOD file from AOD file, e.g.:
# ./createMiniAOD.py --aodfile=root://cmsxrootd.fnal.gov//store/data/Run2018A/MET/AOD/17Sep2018-v1/120000/8B09BCD4-ACB4-D343-823F-9FFF2EC9472E.root --outfile miniaod.root

parser = OptionParser()
parser.add_option('--infile', dest='infile')
parser.add_option('--outfile', dest='outfile')
parser.add_option('--nev', dest='nev')
(options, args) = parser.parse_args()

print 'Creating miniAOD file for AOD:', options.infile

if not 'root://' in options.infile:
    options.infile = 'root://cmsxrootd.fnal.gov/' + options.infile

if '/data/' in options.infile:
    is_data = True
else:
    is_data = False

conditions = {
                'RunIISummer16': ['CMSSW_8_0_21', '80X_mcRun2_asymptotic_2016_TrancheIV_v6', 'Run2_2016'],
                'RunIIFall17': ['CMSSW_9_4_6_patch1', '94X_mc2017_realistic_v11', 'Run2_2017'],
                'Run2016*07Aug17': ['CMSSW_8_0_29', '80X_dataRun2_2016LegacyRepro_v4', 'Run2_2016'],
                'Run2017*17Nov2017': ['CMSSW_9_4_0', '94X_dataRun2_ReReco_EOY17_v1', 'Run2_2017'],
                'Run2018*17Sep2018': ['CMSSW_10_2_4_patch1', '102X_dataRun2_Sep2018Rereco_v1', 'Run2_2018'],
                'Run2018B*PromptReco': ['CMSSW_10_1_5', '101X_dataRun2_Prompt_v10', 'Run2_2018'],
                'Run2018D*PromptReco': ['CMSSW_10_2_0', '102X_dataRun2_Prompt_v1', 'Run2_2018'],
             }

cmssw_version = ""
global_tag = ""
era = ""
for condition in conditions:
    count = 0
    for subcondition in condition.split("*"):
        if subcondition in options.infile:
            count += 1
    if count == len(condition.split("*")):
        # passed all conditions
        cmssw_version = conditions[condition][0]
        global_tag = conditions[condition][1]
        era = conditions[condition][2]

print cmssw_version, global_tag, era
if cmssw_version == "":
    print "Cannot determine which conditions to use for file", options.infile
    exit(50)

if is_data:
    command = 'cmsDriver.py miniAOD-prod -s PAT --eventcontent MINIAOD --runUnscheduled --data --conditions %s --era %s --filein %s --fileout file:%s -n %s' % (global_tag, era, options.infile, options.outfile, options.nev)
else:
    command = 'cmsDriver.py miniAOD-prod -s PAT --eventcontent MINIAODSIM --runUnscheduled --mc --conditions %s --era %s --filein %s --fileout file:%s -n %s' % (global_tag, era, options.infile, options.outfile, options.nev)

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

status, output = commands.getstatusoutput('sh createMiniAOD.sh')

print 'Output status:', status
with open("miniaod.log", "w+") as fout:
    fout.write(output)

if status != 0:
    print output

exit(status)
