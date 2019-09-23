#!/bin/env python
import os
from optparse import OptionParser
import commands
import collections
import json
import glob
import time

# retrieve miniAOD file name from text file catalogue
# format:
# [AOD file]
# corresponding miniAOD file 1
# corresponding miniAOD file 2

parser = OptionParser()
parser.add_option('--infile', dest='infile')
parser.add_option('--test', action='store_true', dest='test')
(options, args) = parser.parse_args()


def read_catalogue(aod_file_name):
    
    for catalogue_name in glob.glob("catalogue_*.dat")
    
        aod_file_name = aod_file_name.replace("/", "\/") 
        command = "sed -n -e '/%s/,/\[/ p' catalogue_%s.dat | head -n -1 | tail -n +2" % (aod_file_name, catalogue_name)
        status, output = commands.getstatusoutput(command)
        miniaod_filenames = output.split("\n")
        
        # fix for multiple versions of miniAOD files present in catalogue:
        miniaod_v1_present = False
        miniaod_v2_present = False
        miniaod_v3_present = False
        for miniaod_filename in miniaod_filenames:
            if "-v1/" in miniaod_filename:
                miniaod_v1_present = True
            elif "-v2/" in miniaod_filename:
                miniaod_v2_present = True
            elif "-v3/" in miniaod_filename:
                miniaod_v2_present = True
        if miniaod_v1_present and miniaod_v2_present:
            print "Multiple versions of miniAODs present, selecting v2 only"
            miniaod_filenames = [x for x in miniaod_filenames if not "-v1/" in x]
        elif miniaod_v1_present and miniaod_v2_present and miniaod_v3_present:
            print "Multiple versions of miniAODs present, selecting v3 only"
            miniaod_filenames = [x for x in miniaod_filenames if not "-v1/" in x and not "-v2/" in x]
        
    if len(miniaod_filenames) > 0:
        print "Found miniAOD files: %s" % str(miniaod_filenames)
        return miniaod_filenames
    else:
        quit("No miniaod file name(s) found")


def get_miniAOD_filenames(aod_file_name):
    
    miniaod_filenames = read_catalogue(aod_file_name)
   
    miniaod_filenames = list(set(miniaod_filenames))
    print "miniaod_filenames", miniaod_filenames
    os.system("echo %s > info_miniaods" % ",".join(miniaod_filenames))

    if options.test:
        print "Test successful", str(miniaod_filenames)
        #return
    
    #first, get start / end of AOD file:
    print "Running edmFileUtil to get run number / lumisec information..."
    if aod_file_name[0:7] == "/store/":
        print "edmFileUtil root://cmsxrootd.fnal.gov/%s -e > TMPFILE" % aod_file_name
        os.system("edmFileUtil root://cmsxrootd.fnal.gov/%s -e > TMPFILE" % aod_file_name)
    else:
        print "edmFileUtil %s -e > TMPFILE" % aod_file_name
        os.system("edmFileUtil %s -e > TMPFILE" % aod_file_name)

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
        output = []
        for i in range(len(runs[run])):
            output.append([runs[run][i], runs[run][i]])
        runs[run] = output

    json_content = json.dumps(runs)
    print "json_content", json_content

    #for data, do intersection with golden json file:
    if "Run201" in aod_file_name:
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
        get_miniAOD_filenames(options.infile)

    else:
        # run some tests:
        print "Running in testing mode"

        print "@@@ Fall17"
        options.infile = "/store/mc/RunIIFall17DRPremix/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/94X_mc2017_realistic_v10-v1/70000/4A9A2A03-7BED-E711-B2C9-5065F38122A1.root"
        get_miniAOD_filenames(options.infile)

        #print "@@@ Summer16"
        #options.infile = "/store/mc/RunIISummer16DR80Premix/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/0C2ECF33-A1C0-E611-9A9C-0CC47A4C8F12.root"
        #get_miniAOD_filenames(options.infile)

        print "@@@ 2016 data"
        options.infile = "/store/data/Run2016B/JetHT/AOD/07Aug17_ver2-v1/50001/84F70C55-397D-E711-8EA4-90B11C0BD63A.root"
        get_miniAOD_filenames(options.infile)

        print "@@@ 2017 data"
        options.infile = "/store/data/Run2017C/SingleElectron/AOD/17Nov2017-v1/80000/6053F038-7EFC-E711-B0DB-0CC47A7C3408.root"
        get_miniAOD_filenames(options.infile)

        print "@@@ 2018 data"
        options.infile = "/store/data/Run2018B/JetHT/AOD/26Sep2018-v1/120000/D80EE4EF-DA75-4B43-A187-42C8DE818C54.root"
        get_miniAOD_filenames(options.infile)

