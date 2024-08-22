import os, sys
from glob import glob

test = False

isfast = True
year = '2017'
#year = '2016'

if year=='2016': scenario = 'Summer16MiniAODv3Fastsig'
if year=='2017': scenario = 'Fall17Fastsig'


if isfast: 
    #minilist = glob('/pnfs/desy.de/cms/tier2/store/user/sbein/CommonSamples/RadiativeMu_2016Fast/v2/higgsino94x_susyall_mChipm*_inMINIAODSIM.root')
    #alreadyglob = ''.join(glob('/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Fast/ntuple_sidecar/*.root'))
    #minilist = glob('/pnfs/desy.de/cms/tier2/store/user/sbein/CommonSamples/RadiativeMu_'+year+'Fast/v3c/higgsino*_inMINIAODSIM.root')
    #alreadyglob = ''.join(glob('/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_'+year+'Fast/ntuple_sidecarv3c/*.root'))
    minilist = glob('/pnfs/desy.de/cms/tier2/store/user/sbein/CommonSamples/RadiativeMu_2017Fast/v3c/higgsino*_inMINIAODSIM.root')
    alreadyglob = ''.join(glob('/pnfs/desy.de/cms/tier2/store/user/sbein/CommonSamples/RadiativeMu_2017Fast/ntuple_sidecarv3c/higgsino*.root')+glob('higgsino*.root'))
else: 
    minilist = glob('/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Full/v2/higgsino94x*_inMINIAODSIM.root')
    alreadyglob = ''.join(glob('/nfs/dust/cms/user/beinsam/CommonSamples/MC_BSM/CompressedHiggsino/RadiativeMu_2016Full/ntuple_sidecar/*.root'))

print 'len(alreadyglob)', len(alreadyglob)

for ijob, minifile in enumerate(minilist):
    outname = minifile.split('/')[-1].split('_inMINIAOD')[0]
    if outname in alreadyglob:
        print 'we got this one already', outname
        continue
    else: print outname, 'will be new'
    
    if not os.path.exists(minifile.replace('_inMINIAODSIM','')):
        print 'skipping due to lack of AOD:', minifile.replace('_inMINIAODSIM','')
        continue

    command = 'cmsRun runMakeTreeFromMiniAOD_cfg.py outfile='+outname+' dataset=file:'+minifile+' scenario='+scenario+' numevents=-1'

    if not isfast: command = command.replace('Fastsig','')
    if not (ijob+1)%7==0: command+=' &'
    print command
    if len(glob('*'+outname+'*'))>0: 
        print 'continuing past', glob('*'+outname+'*')[0]
        continue
    if not test: os.system(command)
    #else: break

