#!/bin/sh
find . -name "*.condor" -delete
find . -name "*stdout" -delete
find . -name "*stderr" -delete
find . -name "jobExecCondor_*jdl" -delete
rm *root *.tar.gz
rm -rf input
mkdir input
