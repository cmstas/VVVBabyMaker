#!/bin/bash

#=====================================
# Setup Root and compile everything
#=====================================

echo "Grabbing Dependancies..."

git clone git@github.com:sgnoohc/CORE.git
cd CORE/
git checkout 2017
cd ..

echo "git checkout submodules"
git submodule update --init --recursive

echo "Setting up ROOT"

export CMSSW_VERSION=CMSSW_9_2_0
export SCRAM_ARCH=slc6_amd64_gcc530
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/cmssw/$CMSSW_VERSION/src
eval `scramv1 runtime -sh`
cd - > /dev/null

export LD_LIBRARY_PATH=$PWD/rooutil:$LD_LIBRARY_PATH

echo "Building CORE, this might take a few minutes..."
cd dilepbabymaker/
source ./localsetup.sh
ln -s ../CORE 
make -j15

echo "Testing the babymaker..."
./dotest.sh
