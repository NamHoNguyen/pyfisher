import sys, os
from ConfigParser import SafeConfigParser 
import cPickle as pickle
import numpy as np
from scipy.interpolate import interp1d
import argparse
from pyfisher.lensInterface import lensNoise
from pyfisher.clFisher import tryLoad, calcFisher, loadFishers, noiseFromConfig, rSigma
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
parser.add_argument('noiseFile', nargs='?',type=bool,help='Use noise files',default=False)

args = parser.parse_args()
expName = args.expName
lensName = args.lensName
saveName = args.saveName
noiseFile = args.noiseFile
print expName,lensName,saveName,noiseFile

TCMB = 2.7255e6

# Read config
iniFile = "input/params_SO.ini"
Config = SafeConfigParser()
Config.optionxform=str
Config.read(iniFile)

outDir = 'output/'+saveName+"_"

if noiseFile:
    fskyList = ['04000','08000','16000']
    noiseList = ['SENS0','SENS1','SENS2']
    efficiencies = np.zeros([len(fskyList),len(noiseList)])
    
else:
    fskyList = ['0']
    noiseList = np.arange(0.25,6,0.5)/np.sqrt(2.)
    efficiencies = []
    obbs = []
    dbbs = []
i = 0
for fskyNow in fskyList:
    j = 0
    for noiseNow in noiseList:
        
        # Get CMB noise functions from external files
        if noiseFile:
            ellT,nlTT,dummy = np.loadtxt('tests/TT/SOV3_T_default1-4-2_noisecurves_deproj0_'+noiseNow+'_mask_'+fskyNow+'_ell_TT_yy.txt',unpack=True)
            ellE,dummy,nlEE = np.loadtxt('tests/EE/Nell_comb_LAT_'+noiseNow+'_fsky'+fskyNow+'.txt',unpack=True)
            tellmin,tellmax = list_from_config(Config,expName,'tellrange')
            pellmin,pellmax = list_from_config(Config,expName,'pellrange')
            fnTT = cosmo.noise_pad_infinity(interp1d(ellT,nlTT,bounds_error=False,fill_value=np.inf),tellmin,tellmax)
            fnEE = cosmo.noise_pad_infinity(interp1d(ellE,nlEE,bounds_error=False,fill_value=np.inf),pellmin,pellmax)
            
            print 'Using noise files for TT and EE'
        else:
            print 'Not using noise files'
        
        
        # Get lensing noise curve. If you want to override something from the Config file in order to make plots varying it,
        # change from None to the value you want.
        if noiseFile:
            ls,Nls,ellbb,dclbb,efficiency,cc = lensNoise(Config,expName,lensName,beamOverride=None,lkneeTOverride=None,lkneePOverride=None,alphaTOverride=None,alphaPOverride=None,noiseFuncT=lambda x: fnTT(x)/TCMB**2.,noiseFuncP=lambda x: fnEE(x)/TCMB**2.)
        else:
            ls,Nls,ellbb,dclbb,efficiency,cc = lensNoise(Config,expName,lensName,beamOverride=None,noiseTOverride=noiseNow,lkneeTOverride=None,lkneePOverride=None,alphaTOverride=None,alphaPOverride=None)
            
        origclbb = dclbb[0]/(1.-efficiency/100.)
        origclbb = np.sqrt(origclbb)*TCMB*180./np.pi*60.
        dclbb = np.sqrt(dclbb[0])*TCMB*180./np.pi*60.

        if noiseFile:
            efficiencies[i,j]=efficiency
        else:
            efficiencies.append(efficiency)
            obbs.append(origclbb)
            dbbs.append(dclbb)
    
        cprint("Delensing efficiency: "+ str(efficiency) + " %",color="green",bold=True)
        j+=1
    i+=1
if noiseFile:
    np.savetxt(outDir+'delensingEff.csv',efficiencies)
else:
    np.savetxt(outDir+'lensingB_delensB_eff.csv',np.vstack([noiseList*np.sqrt(2.),obbs,dbbs,efficiencies]).T)
