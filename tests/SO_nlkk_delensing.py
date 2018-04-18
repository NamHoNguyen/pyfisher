import sys, os
from ConfigParser import SafeConfigParser 
import cPickle as pickle
import numpy as np
from scipy.interpolate import interp1d
import argparse
from pyfisher.lensInterface import lensNoise
from orphics.io import list_from_config, cprint
import orphics.cosmology as cosmo
#from orphics.cosmology import LensForecast
from orphics.io import Plotter

# Get the name of the experiment and lensing type from command line
parser = argparse.ArgumentParser(description='Run a Fisher test.')
parser.add_argument('expName', type=str,help='The name of the experiment in input/params.ini')
parser.add_argument('lensName',type=str,help='The name of the CMB lensing section in input/params.ini. ',default="")
#parser.add_argument('saveName', nargs='?',type=str,help='Suffix for plots ',default="")
parser.add_argument('saveName',type=str,help='Suffix for plots ',default="")

args = parser.parse_args()
expName = args.expName
lensName = args.lensName
saveName = args.saveName
print expName,lensName,saveName

TCMB = 2.7255e6

# Read config
iniFile = "input/params_SO.ini"
Config = SafeConfigParser()
Config.optionxform=str
Config.read(iniFile)

fskyNow = '04000'
timeList = ['1.0','0.5','0.25']
noiseList = ['SENS0','SENS1','SENS2']
nIter = np.inf

if nIter == 1:
    iterName = 'iterOff_'
else:
    iterName = 'iterOn_'

efficiencies = np.zeros([len(timeList),len(noiseList)])
    
fsky = float(fskyNow)/40000.

print "Run with testNlkk lensing, "+iterName
outDir = 'output/'+saveName+'_'
#for noiseNow,fskyNow in zip(noiseList,fskyList):

#cambRoot = '../quicklens/quicklens/data/cl/planck_wp_highL/planck_lensing_wp_highL_bestFit_20130627'
cambRoot = '/home/hnnguyen/CAMB-0.1.6.1/base_plikHM_TT_lowTEB_minimum_fudgedtotaup06_lmax5000'
theoryOverride = cosmo.loadTheorySpectraFromCAMB(cambRoot,unlensedEqualsLensed=False,useTotal=False,TCMB = 2.7255e6,lpad=9000,get_dimensionless=True)
#theoryOverride = None

i = 0
for timeNow in timeList:
    time = float(timeNow)
    j = 0
    for noiseNow in noiseList:
        # Get CMB noise and pad it with inf
        tellmin,tellmax = list_from_config(Config,expName,'tellrange')
        pellmin,pellmax = list_from_config(Config,expName,'pellrange')
        ellT,nlTT,dummy = np.loadtxt('tests/TT/SOV3_T_default1-4-2_noisecurves_deproj0_'+noiseNow+'_mask_'+fskyNow+'_ell_TT_yy.txt',unpack=True)
        #ellE,dummy,nlEE = np.loadtxt('tests/EE/Nell_comb_LAT_'+noiseNow+'_fsky'+fskyNow+'.txt',unpack=True)
        ellE,nlEE,nlBB = np.loadtxt('tests/EE-BB/SOV3_pol_default1-4-2_noisecurves_deproj0_'+noiseNow+'_mask_'+fskyNow+'_ell_EE_BB.txt',unpack=True)
        fnTT = cosmo.noise_pad_infinity(interp1d(ellT,nlTT,bounds_error=False,fill_value=np.inf),tellmin,tellmax)
        fnEE = cosmo.noise_pad_infinity(interp1d(ellE,nlEE,bounds_error=False,fill_value=np.inf),pellmin,pellmax)

        # fnTT is dimensional from file        
        # Pad CMB lensing noise with infinity outside L ranges
        ls,Nls,ellbb,dclbb,efficiency,cc = lensNoise(Config,expName,lensName,beamOverride=None,lkneeTOverride=None,lkneePOverride=None,alphaTOverride=None,alphaPOverride=None,noiseFuncT=lambda x: fnTT(x)/TCMB**2./time,noiseFuncP=lambda x: fnEE(x)/TCMB**2./time,theoryOverride=theoryOverride,nIter=nIter)
        kellmin,kellmax = list_from_config(Config,lensName,'Lrange')
        fnKK = cosmo.noise_pad_infinity(interp1d(ls,Nls,fill_value=np.inf,bounds_error=False),kellmin,kellmax)
        Lrange = np.arange(kellmin,kellmax)
        #np.savetxt(outDir+'nlkk_deproj0_'+noiseNow+'_fksy_'+fskyNow+'_time_'+timeNow+'.csv',np.vstack([Lrange,fnKK(Lrange)]).T)

        efficiencies[i,j]=efficiency
        print fskyNow,timeNow,noiseNow
        cprint("Delensing efficiency: "+ str(efficiency) + " %",color="green",bold=True)
        
        j+=1
    i+=1
np.savetxt(outDir+iterName+'delensingEff.csv',efficiencies)
    
