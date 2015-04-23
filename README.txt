export SCRAM_ARCH=slc6_amd64_gcc481
cmsrel CMSSW_7_2_0
cd CMSSW_7_2_0/src/
cmsenv
git clone git@github.com:gzevi/EgammaWork.git  
scramv1 b -j10 

To make test ntuple:
cd EgammaWork/ElectronNtupler/test
cmsRun runElectrons.py

