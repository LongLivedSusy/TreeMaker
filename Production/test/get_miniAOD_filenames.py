#!/bin/env python
import os
from optparse import OptionParser
import commands
import collections
import json
import time

parser = OptionParser()
parser.add_option('--infile', dest='infile')
parser.add_option('--outfile', dest='outfile')
parser.add_option('--nev', dest='nev')
parser.add_option('--test', action='store_true', dest='test')
(options, args) = parser.parse_args()

number_of_dbs_requests = 0

def get_miniAOD_filenames():

    print 'locating miniAOD file(s) which match the AOD file %s...' % options.infile

    if not 'root://' in options.infile:
        options.infile = 'root://cmsxrootd.fnal.gov/' + options.infile

    global number_of_dbs_requests
    number_of_dbs_requests = 0
    retry_count = 5

    def dataset_is_correct_miniAOD(dataset):
        if ("Run2016B" in options.infile and "/MINIAOD/17Jul2018_ver1-v1/" in dataset) or \
           ("Run2016B" in options.infile and "/MINIAOD/17Jul2018_ver2-v1/" in dataset) or \
           ("Run2016B" in options.infile and "/MINIAOD/17Jul2018_ver2-v2/" in dataset) or \
           ("Run2016C" in options.infile and "/MINIAOD/17Jul2018-v1/" in dataset) or \
           ("Run2016D" in options.infile and "/MINIAOD/17Jul2018-v1/" in dataset) or \
           ("Run2016E" in options.infile and "/MINIAOD/17Jul2018-v1/" in dataset) or \
           ("Run2016F" in options.infile and "/MINIAOD/17Jul2018-v1/" in dataset) or \
           ("Run2016G" in options.infile and "/MINIAOD/17Jul2018-v1/" in dataset) or \
           ("Run2016H" in options.infile and "/MINIAOD/17Jul2018-v1/" in dataset) or \
           ("Run2016H" in options.infile and "/MINIAOD/17Jul2018-v2/" in dataset) or \
           ("Run2017"  in options.infile and "/MINIAOD/31Mar2018-v1/" in dataset) or \
           ("Run2018A" in options.infile and "/MINIAOD/17Sep2018-v1/" in dataset) or \
           ("Run2018B" in options.infile and "/MINIAOD/17Sep2018-v1/" in dataset) or \
           ("Run2018C" in options.infile and "/MINIAOD/17Sep2018-v1/" in dataset) or \
           ("Run2018D" in options.infile and "/MINIAOD/PromptReco-v1/" in dataset) or \
           ("Run2018D" in options.infile and "/MINIAOD/PromptReco-v2/" in dataset) or \
           ("Summer16" in options.infile and "/RunIISummer16MiniAODv2/" in dataset) or \
           ("RunIIFall17" in options.infile and "/RunIIFall17MiniAODv2/" in dataset):
            return True
        else:
            return False


    def run_cmd(command):

        global number_of_dbs_requests

        if number_of_dbs_requests > 40:
            print "Could not locate corresponding miniAOD file, doing too many (%s) DBS requests!" % number_of_dbs_requests
            quit(99)

        print "Running:", command
        exitcode, output = commands.getstatusoutput(command)
        print "[%s] %s" % (exitcode, output)
        number_of_dbs_requests += 1

        return exitcode, output


    def get_miniaod_filenames():

        # get corresponding miniAOD file(s):
        miniaod_filenames = []

        # first check children for miniAODs:
        status, child_filenames = run_cmd('dasgoclient -query="child file=/%s"' % options.infile.split("//")[-1])

        child_filenames = child_filenames.split("\n")
        for child in child_filenames:
            if dataset_is_correct_miniAOD(child):
                miniaod_filenames.append(child)

        # if no matches have been found, check children of parent files for matching miniAODs:

        if len(miniaod_filenames) == 0:
            
            print "Checking children of parent files for matching miniAODs..."
            status, parent_filenames = run_cmd('dasgoclient -query="parent file=/%s"' % options.infile.split("//")[-1])
            for parent_filename in parent_filenames.split("\n"):
            
                status, cousins_filenames = run_cmd('dasgoclient -query="child file=%s"' % parent_filename)
                relatives_filenames = cousins_filenames.split("\n")
            
                for relative in relatives_filenames:
                    if dataset_is_correct_miniAOD(relative):
                        miniaod_filenames.append(relative)

        if len(miniaod_filenames) == 0:
            print "Could not locate corresponding miniAOD file after %s DBS requests!" % number_of_dbs_requests
            return False
        else:
            print "Used %s number of DBS requests to retrieve miniAOD filename(s)" % number_of_dbs_requests
            miniaod_filenames = list(set(miniaod_filenames))
            print "miniaod_filenames", miniaod_filenames
            os.system("echo %s > info_miniaods" % ",".join(miniaod_filenames))
            return True


    successful = get_miniaod_filenames()

    # retry in case no miniAOD filename(s) have been found - there could have been an issue with DBS
    if not successful:
        retry_count -= 1
        if retry_count > 0:
            print "Retrying DBS request, retrying after some time (count %s)" % retry_count
            time.sleep(10)
            run_cmd(command)
        else:
            print "Failed to retrieve miniAOD filename(s)"
            quit(99)

    if options.test:
        print "@@@ Test successful"
        return

    #first, get start / end of AOD file:
    print "Running edmFileUtil to get run number / lumisec information..."
    os.system("edmFileUtil %s -e > TMPFILE" % options.infile)

    #write json file for AOD file:
    runs = collections.OrderedDict()
    with open("TMPFILE", "r") as fin:
        lines = fin.read()
        for i, line in enumerate(lines.split("\n")):
            if i < 7: continue
            if len(line.split()) == 4:
                run = int(line.split()[0])
                lumi = int(line.split()[1])
                if run not in runs:
                    runs[run] = []
                runs[run].append(lumi)
                runs[run] = sorted(list(set(runs[run])))


    for run in runs:
        #runs[run] = [min(runs[run]), max(runs[run])]
        output = []
        for i in range(len(runs[run])):
            output.append([runs[run][i], runs[run][i]])
        runs[run] = output

    json_content = json.dumps(runs)
    print "json_content", json_content

    #for data, do intersection with golden json file:
    if "Run201" in options.infile:
        with open("lumisecs.json", "w") as fo:
             fo.write(json_content)
        os.system("compareJSON.py --and $(cat info_jsonfilename) lumisecs.json > lumisecs_union.json")
    else:
        with open("lumisecs_union.json", "w") as fo:
            fo.write(json_content)

    #check for empty json union:
    with open("lumisecs_union.json", "r") as fin:
        union = fin.read()
        if union == "{}\n":
            print "Empty union, ignoring"
            exit(123)
        
    print "Done"


if __name__ == "__main__":

    if not options.test:
        # normal operation:
        get_miniAOD_filenames()

    else:
        # run some tests:
        print "Running in testing mode"

        print "@@@ Summer16"
        options.infile = "/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0C2ECF33-A1C0-E611-9A9C-0CC47A4C8F12.root"
        get_miniAOD_filenames()

        print "@@@ Fall17"
        options.infile = "/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/4A9A2A03-7BED-E711-B2C9-5065F38122A1.root"
        get_miniAOD_filenames()

        print "@@@ 2016 data"
        options.infile = "/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50001/84F70C55-397D-E711-8EA4-90B11C0BD63A.root"
        get_miniAOD_filenames()

        print "@@@ 2017 data"
        options.infile = "/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/80000/6053F038-7EFC-E711-B0DB-0CC47A7C3408.root"
        get_miniAOD_filenames()

        print "@@@ 2018 data"
        options.infile = "/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/D80EE4EF-DA75-4B43-A187-42C8DE818C54.root"
        get_miniAOD_filenames()

