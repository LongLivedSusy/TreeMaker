#!/bin/env python
import os, sys, glob
from ROOT import *
import datetime as dt
import commands
from collections import OrderedDict 
from optparse import OptionParser
import time
import datetime
from time import gmtime, strftime
import uuid

def get_userlist():
    userlist = []
    hub_folders = glob.glob("/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/")
    for hub_folder in hub_folders:
        if "amohamed" in hub_folder: continue
        userlist.append(hub_folder.split("/")[-3])
    return userlist


def get_uuids_from_pnfs():

    all_files = []
    for username in get_userlist():
        print "Checking for files of %s..." % username
        user_files = glob.glob("/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v3/*.root" % username)
        all_files += [i.split("/")[-1].split("_")[-2] for i in user_files]
    return all_files


def get_uuids_from_filelist(filelist_name):

    all_files = []
    contents = ""
    with open(filelist_name, "r") as fin:
        contents = fin.read()  
    for line in contents.split("\n"):
        if ".root" in line:
            file_name = line.split("'")[1]
            file_name = file_name.split("/")[-2] + "-" + file_name.split("/")[-1].replace(".root", "")
            all_files.append(file_name)
    return all_files

    

def collect_progress(filelist_name, uuids_from_pnfs):

    uuids_from_filelist = get_uuids_from_filelist(filelist_name)
    n_total = len(uuids_from_filelist)
    # for number of finished ntuples, get the intersection between UUIDs from pnfs and the file list:
    n_done = len(list(set(uuids_from_filelist) & set(uuids_from_pnfs)))
    return (n_done, n_total)


def get_progress_dict(treemakerpath):

    uuids_from_pnfs = get_uuids_from_pnfs()

    campaigns = [
             "Run2016B-17Jul2018_ver1-v1",
             "Run2016B-17Jul2018_ver2-v1",
             "Run2016B-17Jul2018_ver2-v2",
             "Run2016C-17Jul2018-v1",
             "Run2016D-17Jul2018-v1",
             "Run2016E-17Jul2018-v1",
             "Run2016F-17Jul2018-v1",
             "Run2016G-17Jul2018-v1",
             "Run2016H-17Jul2018-v1",
             "Run2016H-17Jul2018-v2",
             "Run2017B-31Mar2018-v1",
             "Run2017C-31Mar2018-v1",
             "Run2017D-31Mar2018-v1",
             "Run2017E-31Mar2018-v1",
             "Run2017F-31Mar2018-v1",
             "Run2018A-17Sep2018-v1",
             "Run2018B-17Sep2018-v1",
             #"Run2018B-26Sep2018_HEMmitigation-v1",
             #"Run2018B-26Sep2018_HEM-v1",
             #"Run2018B-26Sep2018-v1",
             "Run2018C-17Sep2018-v1",
             "Run2018D-PromptReco-v1",
             "Run2018D-PromptReco-v2",
             "RunIIFall17MiniAODv2",
             "Summer16",
             "RunIISummer16MiniAODv3",
            ]

    datastreams = ["MC", "EGamma", "JetHT", "MET", "SingleMuon", "SingleElectron"]

    progress = {}

    for campaign in campaigns:

        if campaign not in progress:
            progress[campaign] = {}

        for datastream in datastreams:

            if "Run201" not in campaign:
                if datastream == "MC":
                    datastream = ""
                else:
                    continue
            else:
                if datastream == "MC":
                    continue

            if datastream == "EGamma" and "Run2018" not in campaign: continue
            if "Run2018" in campaign and datastream == "SingleElectron": continue

            filelist_names = treemakerpath + "/Production/python/%s/%s*AOD*_cff.py" % (campaign, datastream)
            n_global_done = 0
            n_global_total = 0
            for filelist_name in glob.glob(filelist_names):

                # only ctau=200 cm signals for RunIISummer16MiniAODv3:
                if campaign == "RunIISummer16MiniAODv3" and not ("SMS-T2bt-LLChipm_ctau-200_mLSP" in filelist_name or "SMS-T1qqqq-LLChipm_ctau-200_mLSP" in filelist_name):
                    continue

                result = collect_progress(filelist_name, uuids_from_pnfs)
                n_global_done += result[0]
                n_global_total += result[1]

            if "Run201" not in campaign:
                datastream = "MC"

            progress[campaign][datastream] = [n_global_done, n_global_total]

            print "%s.%s: %s/%s done" % (campaign, datastream, progress[campaign][datastream][0], progress[campaign][datastream][1])

    return progress


def invert_dict(progress, selected_campaigns = []):

    output = {}

    for label in progress:

        if len(selected_campaigns)>0:
            keep = False
            for selected_campaign in selected_campaigns:
                if selected_campaign in label:
                    keep = True
            if not keep: continue

        print label

        for datastream in progress[label]:

            if datastream == "MC":
                output[label] = [0, 0]
                output[label][0] = progress[label][datastream][0]
                output[label][1] = progress[label][datastream][1]
                continue

            if datastream not in output:
                output[datastream] = [0, 0]

            output[datastream][0] += progress[label][datastream][0]
            output[datastream][1] += progress[label][datastream][1]

    return output
                       

def save_datapoint_to_file(logfile = "progress-monitor.log"):

    progress = get_progress_dict(options.treemakerpath)

    timestamp = datetime.datetime.now()

    with open(logfile, "a") as fout:
        fout.write(str(timestamp) + " = " + str(progress) + "\n")


def produce_html(xvals, yvals_dict, title):

    def get_dataset_html(yvals, label, color):

        if "total" in label:
           return """
                          { 
                            data: %s,
                            label: "%s",
                            borderColor: "%s",
                            fill: false,
                            borderDash: [10,5],
                            display: false,
                          },
                        """ % (yvals, label, color)
        else:
            return """
                      { 
                        data: %s,
                        label: "%s",
                        borderColor: "%s",
                        fill: false,
                      },
                    """ % (yvals, label, color)

    datasets = ""
    for label in yvals_dict:
        yvals = yvals_dict[label]["yvals"]
        ylabel = label
        ycolor = yvals_dict[label]["color"]
        datasets += get_dataset_html(yvals, ylabel, ycolor)

    myuuid = uuid.uuid1()

    template = """
        <canvas id="%s" width="600px" height="200px"></canvas>
        <script language="Javascript">

        new Chart(document.getElementById("%s"), {
          type: 'line',
          data: {
            labels: %s,
            datasets: [
              %s
            ]
          },
          options: {
            responsive: true,
            title: {
              display: true,
              text: '%s'
            }
          }
        });

        </script>
    """ % (myuuid, myuuid, xvals, datasets, title)

    return template
    

def get_plots(selected_campaigns, title):

    contents = ""
    with open("progress-monitor.log", "r") as fin:
        contents = fin.read()

    dates = []
    yvals = OrderedDict()

    webcolors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff']
    webcolors += webcolors

    for line in contents.split("\n"):
        if len(line) == 0: continue

        date = line.split(" = ")[0]
        date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        date = date.strftime("%Y-%m-%d %H:%M:%S")
        progress = eval(line.split(" = ")[1])
        progress = invert_dict(progress, selected_campaigns)

        dates.append(date)
        
        for item in progress:

            color = webcolors.pop(0)

            if item + "_total" not in yvals:
                yvals[item + "_total"] = {"yvals": [], "color": color}
            if item + "_done" not in yvals:
                yvals[item + "_done"] = {"yvals": [], "color": color}

            yvals[item + "_done"]["yvals"].append(progress[item][0])
            yvals[item + "_total"]["yvals"].append(progress[item][1])
   
    html = produce_html(dates, yvals, title)

    return html


if __name__ == "__main__":

    parser = OptionParser()
    parser.add_option("--treemakerpath", dest="treemakerpath", default="./CMSSW_10_2_7/src/TreeMaker/")
    (options, args) = parser.parse_args()

    #save_datapoint_to_file()

    html = """
                <script src="https://www.chartjs.org/dist/2.8.0/Chart.min.js"></script>
           """
    html += "<font face=Arial><h2>Totals:</h2></font>"
    html += get_plots([], "Grand totals")
    html += "<p><hr><p>"
    html += "<h2>Years:</h2></font>"
    html += get_plots(["Run2016"], "2016")
    html += get_plots(["Run2017"], "2017")
    html += get_plots(["Run2018"], "2018")
    html += get_plots(["Summer16", "Fall17"], "MC")

    with open("index.html", "w") as fout:
        fout.write(html)

    os.system("mv index.html ~/www/ntuple-production/index.html")
    



