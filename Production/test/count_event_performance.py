import os, sys, glob
from ROOT import *
import datetime as dt

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
    
    for user in ["vkutzner", "sbein", "tokramer"]:   
        
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
        histos[label].GetYaxis().SetRangeUser(1e-2, 1.2*maximum)
        histos[label].SetTitle("NtupleHub contents, last %s days;last days;gigabytes" % len(data["vkutzner"]))
        
        legend.AddEntry(histos[label], label)
            
    legend.Draw()
    canvas.SaveAs("evtperf.pdf")

data = collect_data(27)

plot(data)