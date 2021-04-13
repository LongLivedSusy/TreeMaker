#!/bin/env python
import os, sys, glob
import datetime as dt
import commands
from collections import OrderedDict 
from optparse import OptionParser
import time
import datetime
from time import gmtime, strftime
import uuid
import json

campaigns = [
              "Run2016B",
              "Run2016C",
              "Run2016D",
              "Run2016E",
              "Run2016F",
              "Run2016G",
              "Run2016H",
              "Run2017B",
              "Run2017C",
              "Run2017D",
              "Run2017E",
              "Run2017F",
              "Run2018A",
              "Run2018B",
              "Run2018C",
              "Run2018D",
            ]

datastreams = ["MET", "SingleElectron", "SingleMuon", "JetHT"]

print "Dataset \t pending/total \t Available datasets"
print "========================================================================================"

for datastream in datastreams:
    for campaign in campaigns:
    
        if "Run2018" in campaign and datastream == "SingleElectron":
            datastream = "EGamma"
    
        status_t, total = commands.getstatusoutput("grep root ~/dust/shorttrack/treemaker/CMSSW_10_2_7/src/TreeMaker/Production/python/*/*AOD*_cff.py | grep %s | grep %s | wc -l" % (campaign, datastream))
        #status_c, completed = commands.getstatusoutput("grep root ~/dust/shorttrack/treemaker/CMSSW_10_2_7/src/TreeMaker/Production/python/*/*AOD*_cff.py | grep %s | grep %s | grep '#' | wc -l" % (campaign, datastream))
        status_p, pending = commands.getstatusoutput("grep root ~/dust/shorttrack/treemaker/CMSSW_10_2_7/src/TreeMaker/Production/python/*/*AOD*_cff.py | grep %s | grep %s | grep '#' -v | wc -l" % (campaign, datastream))
        status_a, availability = commands.getstatusoutput("grep %s samples_available | grep %s" % (campaign, datastream))
        
        if availability == "":
            availability = "on tape..."
        
        print "%s/%s: \t %s/%s \t %s" % (datastream, campaign, pending, total, availability.replace("\n", " "))
        
print "========================================================================================"

status, total = commands.getstatusoutput("grep root ~/dust/shorttrack/treemaker/CMSSW_10_2_7/src/TreeMaker/Production/python/*/*AOD*_cff.py | grep Run201 | grep '#' -v | wc -l")
status, pending = commands.getstatusoutput("grep root ~/dust/shorttrack/treemaker/CMSSW_10_2_7/src/TreeMaker/Production/python/*/*AOD*_cff.py | grep Run201 | wc -l")

print "Total pending/total          %s/%s" % (pending, total)