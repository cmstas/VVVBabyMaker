#!/bin/bash

if [ -z $1 ];then
    echo "Usage:   sh ln.sh VERSION (e.g. WWW2016_v5.1.9)"
    exit
fi

if [[ $1 == *"2016"* ]]; then
    VBSSAMPLENAMEPATTERN="wpwpjj"
else
    VBSSAMPLENAMEPATTERN="vbs"
fi

if [[ $1 == *"2016"* ]]; then
    WWWTOSKIPPATTERN="www_2l"
elif [[ $1 == *"2017"* ]]; then
    WWWTOSKIPPATTERN="www_amcatnlo_private"
elif [[ $1 == *"2018"* ]]; then
    WWWTOSKIPPATTERN="NONE"
fi

if [[ $1 == *"2018"* ]]; then
    VHTOSKIPPATTERN="NONE"
else
    VHTOSKIPPATTERN="vh_nonbb_amcatnlo_dilepfilter"
fi

WGTOSKIP="wg_lvg_madgraph\|wg_lnug_madgraph"

BASEDIR=/nfs-7/userdata/$USER/WWW_babies/

VERSION=$1

cd $BASEDIR

rm -rf $1/grouped/
rm -rf $1/merged/

mkdir -p $1/grouped/
mkdir -p $1/merged/

cd $1/merged/
ln -sf $(ls ../skim/*.root) .

# Some samples are duplicates so erase the link
if [[ $1 == *"2018"* ]]; then
    rm wz_incl_pythia_1.root
    rm ttbar_*_madgraph_*.root
fi

cd ../grouped/
mkdir -p bkg
mkdir -p bkgdata
mkdir -p bkgnonvbsttw
mkdir -p data
mkdir -p sig
mkdir -p sigofficial
mkdir -p sigofficialvh
mkdir -p sigofficialwww
mkdir -p sigvh
mkdir -p sigwww
mkdir -p sigallwwz
mkdir -p sigallwzz
mkdir -p sigallzzz
mkdir -p vvv
mkdir -p ttw
mkdir -p vbs

cd bkg/
echo linking... bkg
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep -v data | grep -v www_ | grep -v wwz_ | grep -v /wzz_ | grep -v zzz_ | grep -v wh_ww | grep -v zh_ww | grep -v wh_zz | grep -v zh_zz | grep -v /vh_nonbb_ | grep -v ${VHTOSKIPPATTERN} | grep -v ${WGTOSKIP}) .
cd ..
cd bkgdata
echo linking... bkgdata
rm -f *.root
# skip wjets_incl because the fake subtractionf or this can often lead to extreme negative subtraction. Not subtracting only leads to more "conservative" estimate of fakes so if anything it will lead to "smaller" sensitivity.
ln -sf $(ls ../../merged/*.root | grep -v www_ | grep -v wwz_ | grep -v /wzz_ | grep -v zzz_ | grep -v wh_ww | grep -v zh_ww | grep -v wh_zz | grep -v zh_zz | grep -v /vh_nonbb_ | grep -v ${VHTOSKIPPATTERN} | grep -v ${WGTOSKIP} | grep -v wjets_incl) .
cd ..
cd bkgnonvbsttw
echo linking... bkgnonvbsttw
rm -f *.root
ln -sf $(ls ../bkg/*.root | grep -v ${VBSSAMPLENAMEPATTERN} | grep -v ttw | grep -v ${WGTOSKIP}) .
cd ..
cd data
echo linking... data
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep data) .
cd ..
cd sig
echo linking... sig
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /www | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep /vh_nonbb_ | grep -v ${VHTOSKIPPATTERN}) .
cd ..
cd sigofficial
echo linking... sigofficial
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /www | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep /vh_nonbb_ | grep -v ${VHTOSKIPPATTERN}) .
cd ..
cd sigofficialvh
echo linking... sigofficialvh
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /vh_nonbb_ | grep -v ${VHTOSKIPPATTERN}) .
cd ..
cd sigofficialwww
echo linking... sigofficialwww
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /www | grep -v ${WWWTOSKIPPATTERN}) .
cd ..
cd sigvh
echo linking... sigvh
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /vh_nonbb_ | grep -v ${VHTOSKIPPATTERN}) .
cd ..
cd sigwww
echo linking... sigwww
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /www | grep -v ${WWWTOSKIPPATTERN}) .
cd ..
cd sigallwwz
echo linking... sigallwwz
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /wwz_ | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep zh_ww | grep -v ${WWWTOSKIPPATTERN}) .
cd ..
cd sigallwzz
echo linking... sigallwzz
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /wzz_ | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep wh_zz | grep -v ${WWWTOSKIPPATTERN}) .
cd ..
cd sigallzzz
echo linking... sigallzzz
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /zzz_ | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep zh_zz | grep -v ${WWWTOSKIPPATTERN}) .
cd ..
cd vvv
echo linking... vvv
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep /zzz_ | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep zh_zz | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep /wzz_ | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep wh_zz | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep /wwz_ | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep zh_ww | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep /www | grep -v ${WWWTOSKIPPATTERN}) .
ln -sf $(ls ../../merged/*.root | grep wh_ww | grep -v ${VHTOSKIPPATTERN}) .
cd ..
cd ttw
echo linking... ttw
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep ttw) .
cd ..
cd vbs
echo linking... vbs
rm -f *.root
ln -sf $(ls ../../merged/*.root | grep ${VBSSAMPLENAMEPATTERN}) .
cd ..


