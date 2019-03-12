#!/bin/env python
import os, sys, glob
from ROOT import *
import datetime as dt
import commands
from collections import OrderedDict 

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
TH1D.SetDefaultSumw2()

def get_userlist():

    # get list of users with NtupleHub at DESY:

    userlist = []
    hub_folders = glob.glob("/pnfs/desy.de/cms/tier2/store/user/*/NtupleHub/")
    for hub_folder in hub_folders:
        userlist.append(hub_folder.split("/")[-3])

    return userlist


def get_entries_last_nth_day(n, folder, timeframe):

    if timeframe == "days":
        now = dt.datetime.now() - dt.timedelta(days=n)
        ago = now - dt.timedelta(days=1)
    elif timeframe == "hours":
        now = dt.datetime.now() - dt.timedelta(hours=n)
        ago = now - dt.timedelta(hours=1)
    
    size = 0
    
    for root, dirs, files in os.walk(folder):  
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)    
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime <= now and mtime > ago:
                size += os.path.getsize(path)
   
    print size
    
    return size
    

def collect_data(days, timeframe):

    counts = {}
    
    now_list = []
    for i_day in range(days):
        if timeframe == "days":
            now = dt.datetime.now() - dt.timedelta(days=i_day)
            now_list.append(now)
        elif timeframe == "hours":
            now = dt.datetime.now() - dt.timedelta(hours=i_day)
            now_list.append(now)

    for user in get_userlist():
        
        print "Checking", user
         
        folder = '/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/' % user             
        counts[user] = [0] * days
                
        for root, dirs, files in os.walk(folder):
            for fname in files:
                path = os.path.join(root, fname)
                st = os.stat(path)    
                mtime = dt.datetime.fromtimestamp(st.st_mtime)

                for i_day, now in enumerate(now_list):
                    if timeframe == "days":
                        ago = now - dt.timedelta(days=1)
                    elif timeframe == "hours":
                        ago = now - dt.timedelta(hours=1)
                    if mtime <= now and mtime > ago:
                        counts[user][i_day] += os.path.getsize(path)
                       
    print counts
    
    return counts


def plot_production_rate(days, timeframe):
    
    data = collect_data(days, timeframe)

    gROOT.SetBatch(True)
    gStyle.SetOptStat(0)
    TH1D.SetDefaultSumw2()
    
    maximum = 0
    minimum = 1e15
    
    histos = {}
    for user in data:
        histos[user] = TH1F(user, user, len(data["vkutzner"])-1, 1, len(data["vkutzner"]))
        for day in range(len(data[user])):
            val = data[user][day] * 1.0/1e9
            histos[user].Fill(day+1, val)
            if val > maximum: maximum = val
            if val != 0 and val < minimum: minimum = val  
    
    print minimum, maximum
    
    canvas = TCanvas("c1", "c1", 800, 800)
    canvas.SetLogy(True)
    
    legend = TLegend(0.7, 0.7, 0.98, 0.94)
    legend.SetTextSize(0.025)    
    
    for i, label in enumerate(histos):
        if i == 0:
            histos[label].Draw("hist")
        else:
            histos[label].Draw("hist same")
        histos[label].SetLineWidth(2)
        histos[label].SetLineColor(i+1)
        histos[label].GetYaxis().SetRangeUser(0.8*minimum, 1.5*maximum)

        if timeframe == "days":
            histos[label].SetTitle("daily production rate, %s;last n days;gigabytes" % (dt.datetime.now().strftime("%b %d %H:%M")))
        elif timeframe == "hours":
            histos[label].SetTitle("hourly production rate, %s;last n hours;gigabytes" % (dt.datetime.now().strftime("%b %d %H:%M")))
        
        legend.AddEntry(histos[label], label)
            
    legend.Draw()
    canvas.SaveAs("evtperf_%s.pdf" % timeframe)
    canvas.SaveAs("evtperf_%s.svg" % timeframe)


def get_dataset_filecount_done(dataset, n):

    now = dt.datetime.now()
    ago = now - dt.timedelta(days=n)
      
    filecount_done = 0 

    folders = []
    for user in get_userlist():
        folders.append("/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v3/" % user)
        if user == "sbein":
            folders.append("/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/ProductionRun2v4/")

    for folder in folders:
        for root, dirs, files in os.walk(folder):  
            for fname in files:
                if dataset in fname:
                    path = os.path.join(root, fname)
                    st = os.stat(path)    
                    mtime = dt.datetime.fromtimestamp(st.st_mtime)
                    if mtime < ago:
                        filecount_done += 1

    print "dataset, n, filecount_done", dataset, n, filecount_done

    return filecount_done


def get_dataset_filecount_done2(datasets, n):

    data = OrderedDict()

    now = dt.datetime.now()
    ago_list = []
    for i_day in range(n):
        ago = now - dt.timedelta(days=i_day)
        ago_list.append(ago)
      
    folders = []
    for user in get_userlist():
        folders.append("/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/ProductionRun2v3/" % user)
        if user == "sbein":
            folders.append("/pnfs/desy.de/cms/tier2/store/user/sbein/NtupleHub/ProductionRun2v4/")

    for dataset in datasets:
        data[dataset] = {}
        data[dataset]["count"] = [0] * n
        data[dataset]["size"] = [0] * n
        data[dataset]["total"] = get_dataset_total(dataset)
   

    for folder in folders:
        print "Searching in folder", folder
        for dataset in datasets:

            status, output = commands.getstatusoutput("ls %s/ | grep %s | head -n 1" % (folder, dataset) )
            output = output.replace("\n", "")

            if len(output) > 0:
                for root, dirs, files in os.walk(folder):  
                    for fname in files:
                        if dataset in fname:
                            path = os.path.join(root, fname)
                            st = os.stat(path)    
                            mtime = dt.datetime.fromtimestamp(st.st_mtime)
                            for i_day, ago in enumerate(ago_list):
                                if mtime < ago:
                                    data[dataset]["count"][i_day] += 1
                                    data[dataset]["size"][i_day] += os.path.getsize(path)

                print " \__> found dataset", dataset, data[dataset]["count"]

    return data


def get_dataset_total(dataset):

    status, filecount_total = commands.getstatusoutput("grep '/store/' ../python/%s*/*AOD*py | wc -l" % dataset)
    print "filecount_total", filecount_total
    return float(filecount_total)
   

def plot_ntuple_count(days):

    datasets = [
                "Run2016B-17Jul2018",
                "Run2016C-17Jul2018",
                "Run2016D-17Jul2018",
                "Run2016E-17Jul2018",
                "Run2016F-17Jul2018",
                "Run2016G-17Jul2018",
                "Run2016H-17Jul2018",
                "Run2017B-31Mar2018",
                "Run2017C-31Mar2018",
                "Run2017D-31Mar2018",
                "Run2017E-31Mar2018",
                "Run2017F-31Mar2018",
                "Run2018A-17Sep2018",
                "Run2018B-17Sep2018",
                "Run2018C-17Sep2018",
                "Run2018D-PromptReco",
               ]

    data = get_dataset_filecount_done2(datasets, days)

    for variable in ["count", "size"]:

        histos = OrderedDict()
        for dataset in datasets:
            histos[dataset] = TH1F(dataset, dataset, len(data["Run2018D-PromptReco"][variable])-1, 1, len(data["Run2018D-PromptReco"][variable]))
            histos[dataset + "_total"] = TH1F(dataset, dataset, len(data["Run2018D-PromptReco"][variable])-1, 1, len(data["Run2018D-PromptReco"][variable]))
            for i in range(len(data[dataset][variable])):
                val = data[dataset][variable][i]
                histos[dataset].Fill(i+1, val)
                histos[dataset + "_total"].Fill(i+1, float(data[dataset]["total"]))

                if variable == "size":
                    histos[dataset].Scale(1.0/1e9)
        
        # plot absolutes:
      
        for period in ["Run2016", "Run2017", "Run2018"]:

            canvas = TCanvas("c1", "c1", 800, 800)
            canvas.SetLogy(False)
            
            legend = TLegend(0.6, 0.7, 0.98, 0.94)
            legend.SetTextSize(0.025)    
            
            colors = range(1,20)
            color = -1

            maximum = 0

            for i, label in enumerate(histos):

                if period not in label: continue

                hmax = histos[label].GetMaximum()
                print period, hmax
                if hmax > maximum: maximum = hmax

                if i == 0:
                    histos[label].Draw("hist")
                else:
                    histos[label].Draw("hist same")
                histos[label].SetLineWidth(2)

                if i%2 == 0:
                    color = colors.pop(0)
                    histos[label].SetLineColor(color)
                else:
                    histos[label].SetLineColor(color)
                    histos[label].SetLineStyle(2)

                xtitle = variable
                if variable == "size":
                    xtitle = "gigabytes"

                histos[label].SetTitle("ntuple %s, %s;last n days;%s" % (variable, dt.datetime.now().strftime("%b %d %H:%M"), xtitle))

                if i%2 == 0:
                    legend.AddEntry(histos[label], label)

            for i, label in enumerate(histos):
                histos[label].GetYaxis().SetRangeUser(0, 1.2*maximum)
                    
            legend.Draw()
            canvas.SaveAs("evtperf2-%s-%s.pdf" % (variable, period) )
            canvas.SaveAs("evtperf2-%s-%s.svg" % (variable, period) )

# plot last 10 hours/days:
plot_production_rate(24, "hours")
plot_production_rate(14, "days")
plot_ntuple_count(14)

# copy to public web folder:
os.system("mv evtperf*svg ~/www/ntuple-production/")
