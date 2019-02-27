#!/bin/env python
import os
from optparse import OptionParser
import commands

parser = OptionParser()
parser.add_option('--infile', dest='infile')
parser.add_option('--outfile', dest='outfile')
parser.add_option('--nev', dest='nev')
(options, args) = parser.parse_args()

print 'locating miniAOD file(s) which match the AOD file:', options.infile

if not 'root://' in options.infile:
    options.infile = 'root://cmsxrootd.fnal.gov/' + options.infile

#get corresponding miniAOD file(s): 
miniaod_filenames = []
status, parent_filenames = commands.getstatusoutput('dasgoclient -query="parent file=/%s"' % options.infile.split("//")[-1])
status, child_filenames = commands.getstatusoutput('dasgoclient -query="child file=/%s"' % options.infile.split("//")[-1])

for parent_filename in parent_filenames.split("\n"):
    status, cousins_filenames = commands.getstatusoutput('dasgoclient -query="child file=%s"' % parent_filename)

    relatives_filenames = cousins_filenames.split("\n") + child_filenames.split("\n")

    for relative in relatives_filenames:
        if   "Run2016B" in options.infile and "/MINIAOD/17Jul2018_ver1-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2016B" in options.infile and "/MINIAOD/17Jul2018_ver2-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2016B" in options.infile and "/MINIAOD/17Jul2018_ver2-v2/" in relative: miniaod_filenames.append(relative)
        elif "Run2016C" in options.infile and "/MINIAOD/17Jul2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2016D" in options.infile and "/MINIAOD/17Jul2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2016E" in options.infile and "/MINIAOD/17Jul2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2016F" in options.infile and "/MINIAOD/17Jul2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2016G" in options.infile and "/MINIAOD/17Jul2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2016H" in options.infile and "/MINIAOD/17Jul2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2016H" in options.infile and "/MINIAOD/17Jul2018-v2/" in relative: miniaod_filenames.append(relative)
        elif "Run2017"  in options.infile and "/MINIAOD/31Mar2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2018A" in options.infile and "/MINIAOD/17Sep2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2018B" in options.infile and "/MINIAOD/17Sep2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2018C" in options.infile and "/MINIAOD/17Sep2018-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2018D" in options.infile and "/MINIAOD/PromptReco-v1/" in relative: miniaod_filenames.append(relative)
        elif "Run2018D" in options.infile and "/MINIAOD/PromptReco-v2/" in relative: miniaod_filenames.append(relative)

    if len(miniaod_filenames) == 0:
        print "Could not locate corresponding miniAOD file!"
        quit(99)

miniaod_filenames = list(set(miniaod_filenames))
print "miniaod_filenames", miniaod_filenames
os.system("echo %s > info_miniaods" % ",".join(miniaod_filenames))


#first, get start / end of AOD file:
print "Running edmFileUtil to get run number / lumisec information..."
os.system("edmFileUtil %s -e > TMPFILE" % options.infile)
status, output = commands.getstatusoutput("grep '(Lumi)' TMPFILE | head -n1")
run_start = output.split()[0]
lumi_start = output.split()[1]
status, output = commands.getstatusoutput("cat TMPFILE | tail -n6 | head -n1")
run_stop = output.split()[0]
lumi_stop = output.split()[1]
aod_range = "%s:%s-%s:%s" % (run_start, lumi_start, run_stop, lumi_stop)


# now, do the union of golden json and custom json:
json_content = '{"%s": [[%s, %s]]}' % (run_start, lumi_start, lumi_stop)
with open("lumisecs.json", "w") as fo:
    fo.write(json_content)
os.system("compareJSON.py --and $(cat info_jsonfilename) lumisecs.json > lumisecs_union.json")


print "Done"
