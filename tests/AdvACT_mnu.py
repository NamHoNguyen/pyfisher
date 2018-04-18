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
parser.add_argument('noiseFilePrefix',nargs='?', type=str,help='Prefix of external noise files',default=None)

args = parser.parse_args()
expName = args.expName
lensName = args.lensName
saveName = args.saveName
noiseFile = args.noiseFilePrefix
print expName,lensName,saveName,noiseFile
# mnu Forecast ============================================

TCMB = 2.7255e6

# Read config
iniFile = "input/params_SO.ini"
Config = SafeConfigParser()
Config.optionxform=str
Config.read(iniFile)

tauList = ['0.01','0.005','0.002']
deprojList = ['0','1','2','3']

fskyNow = '16000'
fsky = float(fskyNow)/40000.

mnus = np.zeros([len(tauList),len(deprojList)])
sns = np.zeros([len(tauList),len(deprojList)])

#for noiseNow,fskyNow in zip(noiseList,fskyList):
i = 0
for tauNow in tauList:
    tau = float(tauNow)
    j = 0
    for deprojNow in deprojList:
        # File root name for Fisher derivatives
        derivRoot = Config.get("fisher","derivRoot")
        
        # Get list of parameters
        paramList = Config.get("fisher","paramList").split(',')
        
        # Load fiducials and derivatives
        fidCls = tryLoad(derivRoot+'_fCls.csv',',')
        dCls = {}
        for paramName in paramList:
            dCls[paramName] = tryLoad(derivRoot+'_dCls_'+paramName+'.csv',',')
            

        fskyScale={'output/savedFisher_HighEllPlanck_fsky0.2.txt':(0.6-fsky)/0.2}

        # Load other Fisher matrices to add
        try:
            otherFisher = loadFishers(Config.get('fisher','otherFishers').split(','),fskyScale)
        except:
            otherFisher = 0.

        # Get CMB noise and pad it with inf
        tellmin,tellmax = list_from_config(Config,expName,'tellrange')
        pellmin,pellmax = list_from_config(Config,expName,'pellrange')
        ellT,nlTT,dummy = np.loadtxt('tests/AdvACT/AdvACT_T_default_Nseasons4.0_NLFyrs2.0_noisecurves_deproj'+deprojNow+'_mask_'+fskyNow+'_ell_TT_yy.txt',unpack=True)
        ellE,nlEE,nlBB = np.loadtxt('tests/AdvACT/AdvACT_pol_default_Nseasons4.0_NLFyrs2.0_noisecurves_deproj'+deprojNow+'_mask_'+fskyNow+'_ell_EE_BB.txt',unpack=True)
        fnTT = cosmo.noise_pad_infinity(interp1d(ellT,nlTT,bounds_error=False,fill_value=np.inf),tellmin,tellmax)
        fnEE = cosmo.noise_pad_infinity(interp1d(ellE,nlEE,bounds_error=False,fill_value=np.inf),pellmin,pellmax)
        
        # fnTT is dimensional from file
        
        # Pad CMB lensing noise with infinity outside L ranges
        ls,Nls = np.loadtxt('output/Apr17_mv_AdvACT_nlkk_deproj'+deprojNow+'_fsky_'+fskyNow+'_iterOn.csv',unpack=True)
        #ls,Nls,ellbb,origclbb,dclbb,efficiency,cc = lensNoise(Config,expName,lensName,beamOverride=None,lkneeTOverride=None,lkneePOverride=None,alphaTOverride=None,alphaPOverride=None,noiseFuncT=lambda x: fnTT(x)/TCMB**2.,noiseFuncP=lambda x: fnEE(x)/TCMB**2.)
        kellmin,kellmax = list_from_config(Config,lensName,'Lrange')
        fnKK = cosmo.noise_pad_infinity(interp1d(ls,Nls,fill_value=np.inf,bounds_error=False),kellmin,kellmax)
        
        # Decide on what ell range to calculate the Fisher matrix
        ellrange = np.arange(min(tellmin,pellmin,kellmin),max(tellmax,pellmax,kellmax)).astype(int)
        # Calculate the Fisher matrix and add to other Fishers
        #Fisher = otherFisher+calcFisher(paramList,ellrange,fidCls,dCls,lambda x: fnTT(x)*TCMB**2.,lambda x: fnEE(x)*TCMB**2.,fnKK,fsky,verbose=True)
        Fisher = otherFisher+calcFisher(paramList,ellrange,fidCls,dCls,lambda x: fnTT(x),lambda x: fnEE(x),fnKK,fsky,verbose=True)

        
        # Get prior sigmas and add to Fisher
        priorList = Config.get("fisher","priorList").split(',')
        print priorList
        priorList[3] = tauNow
        print priorList
        
        for prior,param in zip(priorList,paramList):
            try:
                priorSigma = float(prior)
            except ValueError:
                continue
            ind = paramList.index(param)
            Fisher[ind,ind] += 1./priorSigma**2.

        # get index of mnu and print marginalized constraint
        indMnu = paramList.index('mnu')
        mnu = np.sqrt(np.linalg.inv(Fisher)[indMnu,indMnu])*1000.
        print fskyNow,'deproj'+deprojNow
        cprint("Sum of neutrino masses 1-sigma: "+ str(mnu) + " meV",color="green",bold=True)
        
        mnus[i,j]=mnu
        
        
        # CLKK S/N ============================================

        # Calculate Clkk S/N
        Clkk = fidCls[:,4]
        frange = np.array(range(len(Clkk)))
        snrange = np.arange(kellmin,kellmax)
        LF = cosmo.LensForecast()
        LF.loadKK(frange,Clkk,ls,Nls)
        sn,errs = LF.sn(snrange,fsky,"kk")
        cprint("Lensing autopower S/N: "+ str(sn),color="green",bold=True)

        sns[i,j]=sn
        
        j+=1
    i+=1
outDir = 'output/'+saveName+"_"

np.savetxt(outDir+'mnu.csv',mnus)
np.savetxt(outDir+'sn.csv',sns)
