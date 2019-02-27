import os, sys, glob
from ROOT import *
import datetime as dt
import commands
from collections import OrderedDict 

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
TH1D.SetDefaultSumw2()

userlist = ["vkutzner", "sbein", "jarieger", "tokramer", "ssekmen"]

def get_entries_last_nth_day(n, folder):

    now = dt.datetime.now() - dt.timedelta(days=n)
    ago = now - dt.timedelta(days=1)
    
    tree = TChain('TreeMaker2/PreSelection')
    size = 0
    
    for root, dirs, files in os.walk(folder):  
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)    
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime <= now and mtime > ago:
                #tree.Add(path)
                size += os.path.getsize(path)
    
    entries = tree.GetEntries()
    
    print size
    
    return size
    

def collect_data(days):

    counts = {}
    
    for user in userlist:   
        
        print user
         
        folder = '/pnfs/desy.de/cms/tier2/store/user/%s/NtupleHub/' % user             
        counts[user] = {}
                
        for i in range(days):
            counts[user][i] = get_entries_last_nth_day(i, folder)
                        
    print counts
    
    return counts


def plot(data):
    
    gROOT.SetBatch(True)
    gStyle.SetOptStat(0)
    TH1D.SetDefaultSumw2()
    
    maximum = 0
    minimum = 1e15
    
    histos = {}
    for user in data:
        histos[user] = TH1F(user, user, len(data["vkutzner"])-1, 1, len(data["vkutzner"]))
        for day in data[user]:
            val = data[user][day] * 1.0/1e9
            histos[user].Fill(day+1, val)
            if val > maximum: maximum = val
            if val != 0 and val < minimum: minimum = val  
    
    print minimum, maximum
    
    canvas = TCanvas("c1", "c1", 800, 800)
    canvas.SetLogy(True)
    
    legend = TLegend(0.7, 0.8, 0.98, 0.94)
    legend.SetTextSize(0.025)    
    
    for i, label in enumerate(histos):
        if i == 0:
            histos[label].Draw("hist")
        else:
            histos[label].Draw("hist same")
        histos[label].SetLineWidth(2)
        histos[label].SetLineColor(i+1)
        histos[label].GetYaxis().SetRangeUser(0.8*minimum, 1.2*maximum)
        histos[label].SetTitle("production rate, %s;last n days;gigabytes" % dt.datetime.now().strftime("%b %d %H:%M"))
        
        legend.AddEntry(histos[label], label)
            
    legend.Draw()
    canvas.SaveAs("evtperf.pdf")
    canvas.SaveAs("evtperf.png")


def get_dataset_filecount_done(dataset, n):

    now = dt.datetime.now()
    ago = now - dt.timedelta(days=n)
      
    filecount_done = 0 

    folders = []
    for user in userlist:
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


def get_dataset_total(dataset):

    status, filecount_total = commands.getstatusoutput("grep '/store/' ../python/%s*/*AOD*py | wc -l" % dataset)
    print "filecount_total", filecount_total
    return float(filecount_total)
   

def collect_datasets(days):
 
    data = OrderedDict()

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

    for dataset in datasets:
        data[dataset] = {}
        data[dataset]["count"] = []
        for i in range(days):
            count = get_dataset_filecount_done(dataset, i)
            data[dataset]["count"].append(count)
        data[dataset]["total"] = get_dataset_total(dataset)
        data[dataset]["percentage"] = 1.0 * data[dataset]["count"][0] / data[dataset]["total"]
    print data

    histos = OrderedDict()
    for dataset in datasets:
        histos[dataset] = TH1F(dataset, dataset, len(data["Run2018D-PromptReco"]["count"])-1, 1, len(data["Run2018D-PromptReco"]["count"]))
        histos[dataset + "_total"] = TH1F(dataset, dataset, len(data["Run2018D-PromptReco"]["count"])-1, 1, len(data["Run2018D-PromptReco"]["count"]))
        for i in range(len(data[dataset]["count"])):
            val = data[dataset]["count"][i]
            histos[dataset].Fill(i+1, val)
            histos[dataset + "_total"].Fill(i+1, float(data[dataset]["total"]))
    
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

            histos[label].SetTitle("ntuple count, %s;last n days;" % dt.datetime.now().strftime("%b %d %H:%M"))

            if i%2 == 0:
                legend.AddEntry(histos[label], label)

        for i, label in enumerate(histos):
            histos[label].GetYaxis().SetRangeUser(0, 1.2*maximum)
                
        legend.Draw()
        canvas.SaveAs("evtperf2-%s.pdf" % period)
        canvas.SaveAs("evtperf2-%s.png" % period)

# plot last 10 days:
plot(collect_data(10))
collect_datasets(10)

# copy to public web folder:
os.system("cp evtperf*png ~/www/ntuple-production/")
