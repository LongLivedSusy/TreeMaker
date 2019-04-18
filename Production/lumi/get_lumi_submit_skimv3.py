#!/bin/env python
import os, glob
from GridEngineTools import runParallel
import commands

def get_data_sample_names(folder, globstring = "/*Run201*root"):
    
    samples = []
    for item in glob.glob(folder + globstring):
                
        sample_name = "_".join( item.split("/")[-1].split(".root")[0].split("_")[:-2] )
        samples.append(sample_name)

    samples = list(set(samples))

    return samples
    

def get_userlist():

    # get list of users with NtupleHub at DESY:

    userlist = []
    hub_folders = glob.glob("/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/")
    for hub_folder in hub_folders:
        userlist.append(hub_folder.split("/")[-3])

    return userlist


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


# collect all ntuple sample names:


ntuples = {}
for user in get_userlist():
    if user == "sbein":
        folder = "/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v4" % user
    else:
        folder = "/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v3" % user
    ntuples[user] = get_data_sample_names(folder)
    
print "ntuples", ntuples


do_submit = True
do_combine = False
do_bril = False

if do_submit:

    command = "./get_lumi_json.py $INPUT $OUTPUT"
    output_folder = "output_lumi"
    commands = []
    for user in ntuples:
        if user == "sbein":
            commands += prepare_command_list("/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v4" % user, ntuples[user], output_folder, command = command, files_per_job = 100)
        else:
            commands += prepare_command_list("/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v3" % user, ntuples[user], output_folder, command = command, files_per_job = 100)
            
    do_submission(commands, output_folder, executable = "get_lumi_json.py")


if do_combine:

    import get_lumi_combine
    get_lumi_combine.get_json(years = ["2016", "2017", "2018"], datastreams = ["JetHT", "MET", "SingleElectron", "SingleMuon"])


if do_bril:
    
    os.system("scp *.json get_lumi_bril.py lxplus:~/")
    os.system("ssh -t -A lxplus 'chmod +x ./get_lumi_bril.py; ./get_lumi_bril.py'")
    os.system("scp lxplus:~/*briloutput .")
    os.system("ssh -t -A lxplus 'rm *briloutput'")

