
## Quick start

    git clone --recursive git@github.com:cmstas/WWWAnalysisRun2.git
    cd WWWAnalysisRun2
    cd wwwbabymaker/dilepbabymaker
    source localsetup.sh
    make -j15
    ./processBaby # will print info like below
    USAGE: processBaby <filename> [<max_num_events>] [index] [BabyMode] [type anything to make it verbose]

To run a sample

    ./processBaby /PATH/TO/YOUR/CMS4.root -1 12345 0

Will create

    output_12345.root

In the format for WWW analysis

The ```BabyMode``` determines the baby processing mode

    0 WWWBaby
    1 FRBaby
    2 OSBaby
    3 TnPBaby
    4 AllBaby
    5 POGBaby
    6 LooseBaby
    7 WWWBaby
    8 WVZVeto

## Before modifying

Check out master before modifying in order not to diverge away

    cd wwwbabymaker
    git checkout master
    cd wwwbabymaker/dilepbabymaker/coreutil
    git checkout master

