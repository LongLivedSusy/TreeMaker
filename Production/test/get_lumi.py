#!/bin/env python
import os, glob
from optparse import OptionParser
import json
from ROOT import *

# get integrated lumi

parser = OptionParser()
(options, args) = parser.parse_args()
if len(args) == 0:
    print "usage: ./get_lumi.py <input files> <output json>"
    quit()

output_json_filename = args[-1]

tree = TChain("TreeMaker2/PreSelection")
for iFile in args[:-1]:
    print "Adding", iFile
    tree.Add(iFile)

nev = tree.GetEntries() 

print "Will run over", nev, "events"

runs = {}

for iEv, event in enumerate(tree):

    if (iEv+1) % 10000 == 0:
        PercentProcessed = int( 20 * iEv / nev )
        line = "[" + PercentProcessed*"#" + (20-PercentProcessed)*" " + "]\t" + "Processing event %s / %s" % (iEv + 1, nev)
        print line

    runnum = event.RunNum
    lumisec = event.LumiBlockNum

    if runnum not in runs:
        runs[runnum] = []

    if lumisec not in runs[runnum]:
        runs[runnum].append(lumisec)

# condense lumisections and get proper json output format

runs_compacted = {}
for run in runs:
    if run not in runs_compacted:
        runs_compacted[run] = []
    for lumisec in runs[run]:
        if len(runs_compacted[run]) > 0 and lumisec == runs_compacted[run][-1][-1]+1:
            runs_compacted[run][-1][-1] = lumisec
        else:
            runs_compacted[run].append([lumisec, lumisec])

json_content = json.dumps(runs_compacted)
print json_content

with open(output_json_filename, "w") as fo:
    fo.write(json_content)

