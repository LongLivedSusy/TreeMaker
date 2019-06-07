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

miniaod_args_2016 = "REMINIAOD -s PAT,DQM:@miniAODDQM --runUnscheduled --data --scenario pp --eventcontent MINIAOD,DQM --datatier MINIAOD,DQMIO --customise_unsch PhysicsTools/PatAlgos/slimming/customizeMiniAOD_HcalFixLegacy2016.customizeAll --processName=PAT"

conditions = {
                'RunIISummer16': {'version': 'CMSSW_8_0_21', 'tag': '80X_mcRun2_asymptotic_2016_TrancheIV_v6', 'era': 'Run2_2016'},
                #'RunIIFall17': {'version': 'CMSSW_9_4_6_patch1', 'tag': '94X_mc2017_realistic_v11', 'era': 'Run2_2017'},
                'RunIIFall17': {'version': 'CMSSW_9_4_6_patch1', 'tag': '94X_mc2017_realistic_v14', 'era': 'Run2_2017'},
                
                'Run2016B*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'custom_args': miniaod_args_2016},
                'Run2016C*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'custom_args': miniaod_args_2016},
                'Run2016D*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'custom_args': miniaod_args_2016},
                'Run2016E*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'custom_args': miniaod_args_2016},
                'Run2016F*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'custom_args': miniaod_args_2016},
                'Run2016G*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016,run2_miniAOD_80XLegacy', 'custom_args': miniaod_args_2016},
                'Run2016H*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016,run2_miniAOD_80XLegacy', 'custom_args': miniaod_args_2016},

                'Run2017*17Nov2017': {'version': 'CMSSW_9_4_5_cand1', 'tag': '94X_dataRun2_ReReco_EOY17_v6', 'era': 'Run2_2017'},

                'Run2018*17Sep2018': {'version': 'CMSSW_10_2_4_patch1', 'tag': '102X_dataRun2_Sep2018Rereco_v1', 'era': 'Run2_2018'},
                'Run2018B*PromptReco': {'version': 'CMSSW_10_1_5', 'tag': '101X_dataRun2_Prompt_v10', 'era': 'Run2_2018'},
                'Run2018D*PromptReco': {'version': 'CMSSW_10_2_0', 'tag': '102X_dataRun2_Prompt_v1', 'era': 'Run2_2018'},
             }

cmssw_version = ""
global_tag = ""
era = ""
custom_args = ""
for condition in conditions:
    count = 0
    for subcondition in condition.split("*"):
        if subcondition in options.infile:
            count += 1
    if count == len(condition.split("*")):
        # passed all conditions
        cmssw_version = conditions[condition]["version"]
        global_tag = conditions[condition]["tag"]
        era = conditions[condition]["era"]
        if "custom_args" in conditions[condition]:
            custom_args = conditions[condition]["custom_args"]

print "cmssw_version:", cmssw_version
print "global_tag:", global_tag
print "era:", era
print "custom_args:", custom_args

if cmssw_version == "":
    print "Cannot determine which conditions to use for file", options.infile
    exit(50)

if custom_args != "":
    command = 'cmsDriver.py %s --conditions %s --era %s --filein %s --fileout file:%s -n %s' % (custom_args, global_tag, era, options.infile, options.outfile, options.nev)
elif is_data:
    command = 'cmsDriver.py miniAOD-prod -s PAT --eventcontent MINIAOD --runUnscheduled --data --conditions %s --era %s --filein %s --fileout file:%s -n %s' % (global_tag, era, options.infile, options.outfile, options.nev)
else:
    command = 'cmsDriver.py miniAOD-prod -s PAT --eventcontent MINIAODSIM --runUnscheduled --mc --conditions %s --era %s --filein %s --fileout file:%s -n %s' % (global_tag, era, options.infile, options.outfile, options.nev)

jobscript = '''#!/bin/zsh
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530
cmsrel CMSBASE
cd CMSBASE/src
eval `scramv1 runtime -sh`
echo "running in path: $(pwd)"
echo "running in CMSSW_VERSION: $CMSSW_VERSION"
echo "running in CMSSW_BASE: $CMSSW_BASE"
cd -
COMMAND
'''

fjob = open('createMiniAOD.sh','w')
fjob.write(jobscript.replace('CMSBASE',cmssw_version).replace('COMMAND',command))
fjob.close()

print "Now running cmsDriver command in %s environment:\n%s\n" % (cmssw_version, command)

status, output = commands.getstatusoutput('sh createMiniAOD.sh')

print 'Output status:', status
with open("miniaod.log", "w+") as fout:
    fout.write(output)

if status != 0:
    print output

exit(status)
