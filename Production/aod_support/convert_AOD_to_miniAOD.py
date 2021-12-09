#!/bin/env python
import os
from optparse import OptionParser
import commands

# create miniAOD file from AOD file, e.g.:
# ./convert_AOD_to_miniAOD.py --infile=root://cmsxrootd.fnal.gov//store/data/Run2018A/MET/AOD/17Sep2018-v1/120000/8B09BCD4-ACB4-D343-823F-9FFF2EC9472E.root --outfile miniaod.root --sl6

parser = OptionParser()
parser.add_option('--infile', dest='infile')
parser.add_option('--outfile', dest='outfile')
parser.add_option('--nev', dest='nev', default=-1)
parser.add_option('--sl6', dest='sl6', action="store_true")
(options, args) = parser.parse_args()

# check if already in singularity
if "SINGULARITY_ENVIRONMENT" in os.environ:
    options.sl6 = False
else:
    options.sl6 = True

print 'Creating miniAOD file for AOD:', options.infile

if not '://' in options.infile:
    options.infile = 'root://cmsxrootd.fnal.gov/' + options.infile

if '/data/' in options.infile or '_data_' in options.infile:
    is_data = True
else:
    is_data = False

if 'Autumn18FS' in options.infile or 'Fall17FS' in options.infile:
    is_fastsim = True
else:
    is_fastsim = False


# the process name (RECO, PAT) is specified in scenarios.py

miniaod_args_2016 = "REMINIAOD -s PAT,DQM:@miniAODDQM --runUnscheduled --data --scenario pp --eventcontent MINIAOD,DQM --datatier MINIAOD,DQMIO --customise_unsch PhysicsTools/PatAlgos/slimming/customizeMiniAOD_HcalFixLegacy2016.customizeAll --processName=PAT"
#miniaod_args_2016 = "REMINIAOD -s PAT,DQM:@miniAODDQM --runUnscheduled --data --scenario pp --eventcontent MINIAOD,DQM --datatier MINIAOD,DQMIO --customise_unsch PhysicsTools/PatAlgos/slimming/customizeMiniAOD_HcalFixLegacy2016.customizeAll --processName=RECO"

conditions = {
                'RunIISummer16': {'version': 'CMSSW_8_0_21', 'tag': '80X_mcRun2_asymptotic_2016_TrancheIV_v6', 'era': 'Run2_2016', 'arch': 'slc6_amd64_gcc700'},
                #'RunIIFall17': {'version': 'CMSSW_9_4_6_patch1', 'tag': '94X_mc2017_realistic_v11', 'era': 'Run2_2017', 'arch': 'slc6_amd64_gcc700'},
                'RunIIFall17': {'version': 'CMSSW_9_4_6_patch1', 'tag': '94X_mc2017_realistic_v14', 'era': 'Run2_2017', 'arch': 'slc6_amd64_gcc700'},

                'RunIIFall17FS': {'version': 'CMSSW_9_4_19', 'tag': '94X_mc2017_realistic_v15', 'era': 'Run2_2017', 'arch': 'slc6_amd64_gcc700', 'custom_args': 'miniAOD-prod --runUnscheduled --eventcontent MINIAODSIM --datatier MINIAODSIM --step PAT --geometry DB:Extended --fast'},
                'RunIIFall17__': {'version': 'CMSSW_9_4_19', 'tag': '94X_mc2017_realistic_v15', 'era': 'Run2_2017', 'arch': 'slc6_amd64_gcc700', 'custom_args': 'miniAOD-prod --runUnscheduled --eventcontent MINIAODSIM --datatier MINIAODSIM --step PAT --geometry DB:Extended --fast'},

                'RunIIAutumn18FS': {'version': 'CMSSW_10_2_11_patch1', 'tag': '102X_upgrade2018_realistic_v15', 'era': 'Run2_2018', 'arch': 'slc6_amd64_gcc700', 'custom_args': 'miniAOD-prod --runUnscheduled --eventcontent MINIAODSIM --datatier MINIAODSIM --step PAT --geometry DB:Extended --fast'},
                
                'Run2016B*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'arch': 'slc6_amd64_gcc700', 'custom_args': miniaod_args_2016},
                'Run2016C*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'arch': 'slc6_amd64_gcc700', 'custom_args': miniaod_args_2016},
                'Run2016D*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'arch': 'slc6_amd64_gcc700', 'custom_args': miniaod_args_2016},
                'Run2016E*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'arch': 'slc6_amd64_gcc700', 'custom_args': miniaod_args_2016},
                'Run2016F*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016_HIPM,run2_miniAOD_80XLegacy', 'arch': 'slc6_amd64_gcc700', 'custom_args': miniaod_args_2016},
                'Run2016G*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016,run2_miniAOD_80XLegacy', 'arch': 'slc6_amd64_gcc700', 'custom_args': miniaod_args_2016},
                'Run2016H*07Aug17': {'version': 'CMSSW_9_4_9', 'tag': '94X_dataRun2_v10', 'era': 'Run2_2016,run2_miniAOD_80XLegacy', 'arch': 'slc6_amd64_gcc700', 'custom_args': miniaod_args_2016},

                'Run2017*17Nov2017': {'version': 'CMSSW_9_4_5_cand1', 'tag': '94X_dataRun2_ReReco_EOY17_v6', 'era': 'Run2_2017', 'arch': 'slc6_amd64_gcc700'},

                'Run2018*17Sep2018': {'version': 'CMSSW_10_2_4_patch1', 'tag': '102X_dataRun2_Sep2018Rereco_v1', 'era': 'Run2_2018', 'arch': 'slc6_amd64_gcc700'},
                'Run2018B*PromptReco': {'version': 'CMSSW_10_1_5', 'tag': '101X_dataRun2_Prompt_v10', 'era': 'Run2_2018', 'arch': 'slc6_amd64_gcc700'},
                'Run2018D*PromptReco': {'version': 'CMSSW_10_2_0', 'tag': '102X_dataRun2_Prompt_v1', 'era': 'Run2_2018', 'arch': 'slc6_amd64_gcc700'},
             }

cmssw_version = ""
global_tag = ""
era = ""
custom_args = ""
scram_arch = ""
for condition in conditions:
    
    if is_fastsim and not ("FS" in condition or "__" in condition):
        continue
    
    count = 0
    for subcondition in condition.split("*"):
        if subcondition in options.infile:
            count += 1
    if count == len(condition.split("*")):
        # passed all conditions
        cmssw_version = conditions[condition]["version"]
        global_tag = conditions[condition]["tag"]
        era = conditions[condition]["era"]
        scram_arch = conditions[condition]["arch"]
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
    command = 'cmsDriver.py miniAOD-prod -s PAT --processName=PAT --eventcontent MINIAOD --runUnscheduled --data --conditions %s --era %s --filein %s --fileout file:%s -n %s' % (global_tag, era, options.infile, options.outfile, options.nev)
else:
    command = 'cmsDriver.py miniAOD-prod -s PAT --processName=PAT --eventcontent MINIAODSIM --runUnscheduled --mc --conditions %s --era %s --filein %s --fileout file:%s -n %s' % (global_tag, era, options.infile, options.outfile, options.nev)

jobscript = '''#!/bin/zsh
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=%s
cd $(mktemp -d)
#cd $TMPDIR
cmsrel CMSBASE
cd CMSBASE/src
eval `scramv1 runtime -sh`
echo "running in path: $(pwd)"
echo "running in CMSSW_VERSION: $CMSSW_VERSION"
echo "running in CMSSW_BASE: $CMSSW_BASE"
cd -
COMMAND
''' % scram_arch

fjob = open('createMiniAOD.sh','w')
fjob.write(jobscript.replace('CMSBASE',cmssw_version).replace('COMMAND',command))
fjob.close()

print "Now running cmsDriver command in %s environment:\n%s\n" % (cmssw_version, command)

# SL6 support
if options.sl6 and "slc6" in scram_arch:
    print "SL6 enabled"
    cwd = os.getcwd()
    status, output = commands.getstatusoutput("singularity exec --contain --bind /afs:/afs --bind /nfs:/nfs --bind /pnfs:/pnfs --bind /cvmfs:/cvmfs --bind /var/lib/condor:/var/lib/condor --bind /tmp:/tmp --pwd . ~/dust/slc6_latest.sif sh -c 'cd %s; sh createMiniAOD.sh'" % cwd)
    print output
else:
    status, output = commands.getstatusoutput('sh createMiniAOD.sh')
    print output

print 'Output status:', status
with open("miniaod.log", "w+") as fout:
    fout.write(output)

if status != 0:
    print output

exit(status)
