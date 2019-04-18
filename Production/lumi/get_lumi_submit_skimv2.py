#!/bin/env python
import os, glob
from GridEngineTools import runParallel
import commands

def prepare_command_list(ntuples_folder, samples, output_folder, files_per_job = 5, files_per_sample = -1, command = "./get_lumi_json.py $INPUT $OUTPUT", nowildcard=False):

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


def do_submission(commands, output_folder, executable = "get_lumi_json.py", runmode = "grid"):

    raw_input("submit %s jobs?" % len(commands))
    os.system("mkdir -p %s" % output_folder)
    os.system("cp %s %s/" % (executable, output_folder))
    runParallel(commands, runmode, dontCheckOnJobs=True)


Production2016v2 = [
                    "Run2016B-03Feb2017_ver2-v2.SingleElectron",
                    "Run2016C-03Feb2017-v1.SingleElectron",
                    "Run2016D-03Feb2017-v1.SingleElectron",
                    "Run2016E-03Feb2017-v1.SingleElectron",
                    "Run2016F-03Feb2017-v1.SingleElectron",
                    "Run2016G-03Feb2017-v1.SingleElectron",
                    "Run2016H-03Feb2017_ver2-v1.SingleElectron",
                    "Run2016H-03Feb2017_ver3-v1.SingleElectron",
                    "Run2016B-03Feb2017_ver2-v2.SingleMuon",
                    "Run2016C-03Feb2017-v1.SingleMuon",
                    "Run2016D-03Feb2017-v1.SingleMuon",
                    "Run2016E-03Feb2017-v1.SingleMuon",
                    "Run2016F-03Feb2017-v1.SingleMuon",
                    "Run2016G-03Feb2017-v1.SingleMuon",
                    "Run2016H-03Feb2017_ver2-v1.SingleMuon",
                    "Run2016H-03Feb2017_ver3-v1.SingleMuon",
                    "Run2016B-03Feb2017_ver2-v2.MET",
                    "Run2016C-03Feb2017-v1.MET",
                    "Run2016D-03Feb2017-v1.MET",
                    "Run2016E-03Feb2017-v1.MET",
                    "Run2016F-03Feb2017-v1.MET",
                    "Run2016G-03Feb2017-v1.MET",
                    "Run2016H-03Feb2017_ver2-v1.MET",
                    "Run2016H-03Feb2017_ver3-v1.MET",
                 ]
                 
ProductionRun2v2 = [
                    "Run2016C-17Jul2018-v1.JetHT",
                    "Run2016E-17Jul2018-v1.JetHT",
                    "Run2016F-17Jul2018-v1.JetHT",
                    "Run2016G-17Jul2018-v1.JetHT",
                    "Run2016H-17Jul2018-v1.JetHT",
                 ]
                 

Run20172018_ntuples = [
                    "ProductionRun2v2Run2017B-31Mar2018-v1.JetHT",
                    "ProductionRun2v2Run2017B-31Mar2018-v1.MET",
                    "ProductionRun2v2Run2017B-31Mar2018-v1.SingleElectron",
                    "ProductionRun2v2Run2017B-31Mar2018-v1.SingleMuon",
                    "ProductionRun2v2Run2017C-31Mar2018-v1.JetHT",
                    "ProductionRun2v2Run2017C-31Mar2018-v1.MET",
                    "ProductionRun2v2Run2017C-31Mar2018-v1.SingleElectron",
                    "ProductionRun2v2Run2017C-31Mar2018-v1.SingleMuon",
                    "ProductionRun2v2Run2017D-31Mar2018-v1.JetHT",
                    "ProductionRun2v2Run2017D-31Mar2018-v1.MET",
                    "ProductionRun2v2Run2017E-31Mar2018-v1.JetHT",
                    "ProductionRun2v2Run2017F-31Mar2018-v1.JetHT",
                    "ProductionRun2v2Run2017F-31Mar2018-v1.MET",
                    "Run2018A-17Sep2018-v1.JetHT",
                    "Run2018A-17Sep2018-v1.MET",
                    "Run2018A-17Sep2018-v1.SingleMuon",
                    "Run2018B-17Sep2018-v1.JetHT",
                    "Run2018B-17Sep2018-v1.MET",
                    "Run2018B-17Sep2018-v1.SingleMuon",
                    "Run2018C-17Sep2018-v1.JetHT",
                    "Run2018C-17Sep2018-v1.MET",
                    "Run2018C-17Sep2018-v1.SingleMuon",
                      ]

do_submit = False
do_combine = False
do_bril = True

if do_submit:

    command = "./get_lumi_json.py $INPUT $OUTPUT"
    output_folder = "output_lumi"
    commands = []
    commands += prepare_command_list("/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/Production2016v2", Production2016v2, output_folder, command = command, files_per_job = 2)
    commands += prepare_command_list("/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/ProductionRun2v2", ProductionRun2v2, output_folder, command = command, files_per_job = 2)
    commands += prepare_command_list("/pnfs/desy.de/cms/tier2/store/user/vkutzner/NtupleHub", Run20172018_ntuples, output_folder, command = command, files_per_job = 2)
    do_submission(commands, output_folder, executable = "get_lumi_json.py")


if do_combine:

    import get_lumi_combine
    #get_lumi_combine.get_json(years = ["2016"], datastreams = ["JetHT", "MET", "SingleElectron", "SingleMuon"])
    get_lumi_combine.get_json(years = ["2016"], datastreams = ["JetHT"])
    get_lumi_combine.get_json(years = ["2017", "2018"], datastreams = ["MET", "SingleElectron", "SingleMuon", "JetHT"])


if do_bril:
    
    os.system("scp *.json get_lumi_bril.py lxplus:~/")
    os.system("ssh -t -A lxplus 'chmod +x ./get_lumi_bril.py; ./get_lumi_bril.py'")
    os.system("scp lxplus:~/*briloutput .")
    os.system("ssh -t -A lxplus 'rm *briloutput'")

