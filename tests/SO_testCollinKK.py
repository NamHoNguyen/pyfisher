import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import itertools
import matplotlib as mpl
mpl.rcParams.update({'font.family':'serif'})
mpl.rcParams.update({'mathtext.fontset':'cm'})
mpl.rcParams.update({'font.size': 18})
mpl.rcParams['lines.linewidth'] = 3

fig = plt.figure(figsize=(10,8))

color = itertools.cycle(['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'])
#for dep in ['0','1','2','3']:
for sens in ['0','1','2']:
    for fsky in ['04000','08000','16000']:
        #KK = np.loadtxt('output/Mar31_EB_nlkk_deproj0_SENS'+sens+'_fsky_'+fsky+'.csv')
        #CollinKK = np.loadtxt('tests/KK-EB/SOV3_pol_default1-4-2_noisecurves_deproj0_SENS'+sens+'_mask_'+fsky+'_L_kk.txt')
        KK = np.loadtxt('output/Mar31_TT_nlkk_deproj0_SENS'+sens+'_fsky_'+fsky+'.csv')
        CollinKK = np.loadtxt('tests/KK-TT/SOV3_T_default1-4-2_noisecurves_deproj0_SENS'+sens+'_mask_'+fsky+'_L_kk.txt')
        KK1 = interp1d(KK[:,0],KK[:,1],bounds_error=False,fill_value=np.inf)
        KK2 = interp1d(CollinKK[:,0],CollinKK[:,1],bounds_error=False,fill_value=np.inf)
        ell = np.arange(50,2900,1)
        c = color.next()
        plt.loglog(ell,KK1(ell),c,label='SENS'+sens+'_fsky_'+fsky)
        plt.loglog(ell,KK2(ell),c+'--')
        print max(KK1(ell)/KK2(ell))
plt.xlabel('$\kappa$',fontsize=20)
plt.ylabel('$N_L^{\kappa\kappa}$',fontsize=20)
plt.title('deproj0-TT')
plt.legend()
#plt.show()
plt.savefig('tests/Apr1_SO_nlkk_TT_compare.png')
