import sys, os
from ConfigParser import SafeConfigParser 
import numpy as np
from scipy.interpolate import interp1d
import argparse
from pyfisher.clFisher import tryLoad, calcFisher
from orphics.io import list_from_config, cprint
import orphics.cosmology as cosmo
'''
Calculate and save SO Fisher matrices for Collins
- deproj0 only, goal and baseline, all fsky
- No other Fisher matrices
- No priors
- CMB Primary only -> lensing=False
- lcdm+mnu
- no w because primary CMB doesn't have w information (matter dominates at decoupling)
'''

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
outDir = 'output/'+saveName+"_"

# Read config
iniFile = "input/params_SO.ini"
Config = SafeConfigParser()
Config.optionxform=str
Config.read(iniFile)

fskyList = ['04000','08000','16000']
noiseList = ['SENS0','SENS1','SENS2']

for fskyNow in fskyList:
    fsky = float(fskyNow)/40000.
    for noiseNow in noiseList:

        derivRoot = Config.get("fisher","derivRoot")
        paramList = Config.get("fisher","paramList").split(',')
        fidCls = tryLoad(derivRoot+'_fCls.csv',',')
        dCls = {}
        for paramName in paramList:
            dCls[paramName] = tryLoad(derivRoot+'_dCls_'+paramName+'.csv',',')
            
        # Get CMB noise and pad it with inf
        tellmin,tellmax = list_from_config(Config,expName,'tellrange')
        pellmin,pellmax = list_from_config(Config,expName,'pellrange')
        ellT,nlTT,dummy = np.loadtxt('tests/TT/SOV3_T_default1-4-2_noisecurves_deproj0_'+noiseNow+'_mask_'+fskyNow+'_ell_TT_yy.txt',unpack=True)

        ellE,nlEE,nlBB = np.loadtxt('tests/EE-BB/SOV3_pol_default1-4-2_noisecurves_deproj0_'+noiseNow+'_mask_'+fskyNow+'_ell_EE_BB.txt',unpack=True)
        fnTT = cosmo.noise_pad_infinity(interp1d(ellT,nlTT,bounds_error=False,fill_value=np.inf),tellmin,tellmax)
        fnEE = cosmo.noise_pad_infinity(interp1d(ellE,nlEE,bounds_error=False,fill_value=np.inf),pellmin,pellmax)
        
        # fnTT is dimensional from file
        
        # Pad CMB lensing noise with infinity outside L ranges
        ls,Nls = np.loadtxt('output/Apr17_mv_nlkk_deproj0_'+noiseNow+'_fsky_'+fskyNow+'_iterOn.csv',unpack=True)
        kellmin,kellmax = list_from_config(Config,lensName,'Lrange')
        fnKK = cosmo.noise_pad_infinity(interp1d(ls,Nls,fill_value=np.inf,bounds_error=False),kellmin,kellmax)
        
        # Decide on what ell range to calculate the Fisher matrix
        ellrange = np.arange(min(tellmin,pellmin,kellmin),max(tellmax,pellmax,kellmax)).astype(int)
        # Calculate the Fisher matrix and add to other Fishers        
        print paramList
        Fisher = calcFisher(paramList,ellrange,fidCls,dCls,lambda x: fnTT(x),lambda x: fnEE(x),fnKK,fsky,verbose=True,lensing=False)
        np.savetxt(outDir+'SOFisher_LCDM+mnu_CMBPrimary_deproj0_'+noiseNow+'_fsky_'+fskyNow+'.csv',Fisher)
