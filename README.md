
## Quick start

    git clone --recursive git@github.com:cmstas/WWWAnalysisRun2.git
    cd WWWAnalysisRun2
    cd wwwbabymaker/dilepbabymaker
    source localsetup.sh
    make -j15 && sh dotest.sh 10000 testjobs_2017.txt

## Before modifying

Check out master before modifying in order not to diverge away

    cd wwwbabymaker
    git checkout master
    cd wwwbabymaker/dilepbabymaker/coreutil
    git checkout master

