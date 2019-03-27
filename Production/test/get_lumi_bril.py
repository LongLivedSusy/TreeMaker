#!/bin/env python
import glob
import os

for json in glob.glob("*.json"):
    os.system("brilcalc lumi -u /fb -i %s > %s" % (json, json + ".briloutput"))   

os.system("mkdir -p processed_jsons")
os.system("cp *json processed_jsons/")