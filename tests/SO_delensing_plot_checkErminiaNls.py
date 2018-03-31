import numpy as np
import matplotlib.pyplot as plt

fskyList = ['04000'] #,'08000','16000']
noiseList = ['SENS0'] #,'SENS1','SENS2']

for fsky in fskyList:
    for noise in noiseList:
        Nl1 = np.loadtxt('tests/TT/SOV3_T_default1-4-2_noisecurves_deproj0_'+noise+'_mask_'+fsky+'_ell_TT_yy.txt')
        Nl2 = np.loadtxt('tests/EE/Nell_comb_LAT_'+noise+'_fsky'+fsky+'.txt')
        
        plt.loglog(Nl1[:,0],Nl1[:,1],label="Collin's TT "+fsky+"_"+noise)
        plt.loglog(Nl2[:,0],Nl2[:,1],label="Erminia's TT "+fsky+"_"+noise)
        plt.loglog(Nl2[:,0],Nl2[:,2],label="Erminia's EE "+fsky+"_"+noise)
plt.xlabel("$\ell$")
plt.ylabel("$N_{\ell}$")
        
plt.legend()
#plt.savefig("tests/Feb17_checkTT.png")
plt.show()
