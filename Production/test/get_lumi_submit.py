#!/bin/env python
import os, glob
from GridEngineTools import runParallel

def prepare_command_list(ntuples_folder, samples, output_folder, files_per_job = 5, files_per_sample = -1, command = "./get_lumi.py $INPUT $OUTPUT", nowildcard=False):

    commands = []

    for sample in samples:

        ifile_list = sorted(glob.glob(ntuples_folder + "/" + sample + "*.root"))

        if nowildcard:
            ifile_list = sorted(glob.glob(ntuples_folder + "/" + sample + ".root"))
        
        if files_per_sample != -1:
            ifile_list = ifile_list[:files_per_sample]
        
        if len(ifile_list)==0:
            continue

        print "Looping over %s files (%s)" % (len(ifile_list), sample)
       
        file_segments = [ifile_list[x:x+files_per_job] for x in range(0,len(ifile_list),files_per_job)]

        for inFile_segment in file_segments:
                
            out_tree = output_folder + "/" + inFile_segment[0].split("/")[-1].split(".root")[0] + ".json"
            cmd = command.replace("$INPUT", str(inFile_segment).replace(", ", ",").replace("[", "").replace("]", ""))
            cmd = cmd.replace("$OUTPUT", out_tree)
            commands.append(cmd)
                        
    return commands


def do_submission(commands, output_folder, executable = "get_lumi.py", runmode = "grid"):

    raw_input("submit %s jobs?" % len(commands))
    os.system("mkdir -p %s" % output_folder)
    os.system("cp %s %s/" % (executable, output_folder))
    runParallel(commands, runmode, dontCheckOnJobs=True)


Run2016_ntuples_2016v2 = [
                    "Run2016B-03Feb2017_ver2-v2.SingleElectron",
                    "Run2016C-03Feb2017-v1.SingleElectron",
                    "Run2016D-03Feb2017-v1.SingleElectron",
                    "Run2016E-03Feb2017-v1.SingleElectron",
                    "Run2016F-03Feb2017-v1.SingleElectron",
                    "Run2016G-03Feb2017-v1.SingleElectron",
                    "Run2016H-03Feb2017_ver2-v1.SingleElectron",
                    "Run2016B-03Feb2017_ver2-v2.SingleMuon",
                    "Run2016C-03Feb2017-v1.SingleMuon",
                    "Run2016D-03Feb2017-v1.SingleMuon",
                    "Run2016E-03Feb2017-v1.SingleMuon",
                    "Run2016F-03Feb2017-v1.SingleMuon",
                    "Run2016G-03Feb2017-v1.SingleMuon",
                    "Run2016H-03Feb2017_ver2-v1.SingleMuon",
                    "Run2016B-03Feb2017_ver2-v2.MET",
                    "Run2016C-03Feb2017-v1.MET",
                    "Run2016D-03Feb2017-v1.MET",
                    "Run2016E-03Feb2017-v1.MET",
                    "Run2016F-03Feb2017-v1.MET",
                    "Run2016G-03Feb2017-v1.MET",
                    "Run2016H-03Feb2017_ver2-v1.MET",
                 ]

do_submit = True
do_combine = True
do_bril = True

if do_submit:

    command = "./get_lumi.py $INPUT $OUTPUT"
    output_folder = "output_lumi"
    commands = []
    commands += prepare_command_list("/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/Production2016v2", Run2016_ntuples_2016v2, output_folder, command = command, files_per_job = 3)
    do_submission(commands, output_folder, executable = "get_lumi.py")


#if do_combine:
#    for datastream in ["MET", "SingleElectron", "SingleMuon", "JetHT"]:
#        os.system("cat 2016*%s*json | sed 's/}{/, /g' | sed 's/, ,/, /g'  > output_2016_%s.json" % (datastream, datastream))



