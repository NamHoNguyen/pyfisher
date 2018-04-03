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

deprojList = ['0','1','2','3']

print "Run with testNlkk lensing or lensTT"
outDir = 'output/'+saveName+"_"
#for noiseNow,fskyNow in zip(noiseList,fskyList):
i = 0

cambRoot = '../quicklens/quicklens/data/cl/planck_wp_highL/planck_lensing_wp_highL_bestFit_20130627'
theoryOverride = cosmo.loadTheorySpectraFromCAMB(cambRoot,unlensedEqualsLensed=False,useTotal=False,TCMB = 2.7255e6,lpad=9000,get_dimensionless=True)
#theoryOverride = None

for deprojNow in deprojList:
    # Get CMB noise and pad it with inf
    tellmin,tellmax = list_from_config(Config,expName,'tellrange')
    pellmin,pellmax = list_from_config(Config,expName,'pellrange')
    #ellT,nlTT,dummy = np.loadtxt('tests/TT/SOV3_T_default1-4-2_noisecurves_deproj1_'+noiseNow+'_mask_'+fskyNow+'_ell_TT_yy.txt',unpack=True)
    ellT,nlTT,dummy = np.loadtxt('tests/AdvACT/AdvACT_T_default_Nseasons4.0_NLFyrs2.0_noisecurves_deproj'+deprojNow+'_mask_16000_ell_TT_yy.txt',unpack=True)
    #ellE,nlEE,nlBB = np.loadtxt('tests/EE-BB/SOV3_pol_default1-4-2_noisecurves_deproj1_'+noiseNow+'_mask_'+fskyNow+'_ell_EE_BB.txt',unpack=True)
    ellE,nlEE,nlBB = np.loadtxt('tests/AdvACT/AdvACT_pol_default_Nseasons4.0_NLFyrs2.0_noisecurves_deproj'+deprojNow+'_mask_16000_ell_EE_BB.txt',unpack=True)
    fnTT = cosmo.noise_pad_infinity(interp1d(ellT,nlTT,bounds_error=False,fill_value=np.inf),tellmin,tellmax)
    fnEE = cosmo.noise_pad_infinity(interp1d(ellE,nlEE,bounds_error=False,fill_value=np.inf),pellmin,pellmax)
    
    # fnTT is dimensional from file        
    # Pad CMB lensing noise with infinity outside L ranges
    ls,Nls,ellbb,dclbb,efficiency,cc = lensNoise(Config,expName,lensName,beamOverride=None,lkneeTOverride=None,lkneePOverride=None,alphaTOverride=None,alphaPOverride=None,noiseFuncT=lambda x: fnTT(x)/TCMB**2.,noiseFuncP=lambda x: fnEE(x)/TCMB**2.,theoryOverride=theoryOverride)
    kellmin,kellmax = list_from_config(Config,lensName,'Lrange')
    fnKK = cosmo.noise_pad_infinity(interp1d(ls,Nls,fill_value=np.inf,bounds_error=False),kellmin,kellmax)
    Lrange = np.arange(kellmin,kellmax)
    np.savetxt(outDir+'AdvACT_nlkk_deproj'+deprojNow+'_fsky_16000.csv',np.vstack([Lrange,fnKK(Lrange)]).T)
    i+=1

