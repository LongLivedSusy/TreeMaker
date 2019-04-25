#!/bin/env python
import os, glob
from GridEngineTools import runParallel
import commands

# submit signal samples to local condor cluster, e.g. BIRD at DESY

status, file_names = commands.getstatusoutput("grep file:// ../python/PrivateSamples/g1800_chi1400_27_200970_CMSSW8_cff")
#status, file_names = commands.getstatusoutput("grep file:// ../python/PrivateSamples/g1800_chi1400_27_200970_CMSSW10_cff")
output_folder = "/nfs/dust/cms/user/kutznerv/DisappTrksSignalMC/newdedx"
scenario = "Summer16sig"
inputFilesConfig = "PrivateSamples.g1800_chi1400_27_200970_CMSSW8"

commands = []

file_names = file_names.split("\n")
for i, file_name in enumerate(file_names):

    file_name = file_name.split("'")[1]
    file_name = file_name.split("/")[-1].replace(".root", "")

    commands.append( "cmsRun runMakeTreeFromMiniAOD_cfg.py scenario=%s inputFilesConfig=%s nstart=%s nfiles=1 outfile=%s; mv %s %s/" % (scenario, inputFilesConfig, i, file_name, file_name + "*.root", output_folder) )

def do_submission(commands, runmode="grid", dontCheckOnJobs=True):

    print "Submitting %s jobs." % len(commands)
    raw_input("Continue?")
    runParallel(commands, runmode, dontCheckOnJobs=dontCheckOnJobs)

print commands

#do_submission(commands)

