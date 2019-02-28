import os, sys, glob
from ROOT import *
output_filename = glob.glob('*RA2AnalysisTree.root')[0]
print "Checking file for tree collection:", output_filename
fin = TFile(output_filename, 'read')
tree = fin.Get('TreeMaker2/PreSelection')
if tree.GetBranch('tracks'):
    print 'tracks present, file OK'
else:
    print 'no tracks collection, deleting output file and failing job'
    os.system('rm ' + output_filename)
    sys.exit(919191)

