import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import itertools
import matplotlib as mpl
mpl.rcParams.update({'font.family':'serif'})
mpl.rcParams.update({'mathtext.fontset':'cm'})
mpl.rcParams.update({'font.size': 18})
mpl.rcParams['lines.linewidth'] = 3


color = itertools.cycle(['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'])
'''
for dep in ['0','1','2','3']:
    for sens in ['0','1','2']:
        for fsky in ['04000','08000','16000']:
            plt.figure(figsize=(10,8))
            c = color.next()
            Apr1 = np.loadtxt('tests/Apr1_mv_L_kk/Apr1_mv_nlkk_deproj'+dep+'_SENS'+sens+'_fsky_'+fsky+'.csv')
            Apr17On = np.loadtxt('output/Apr17_mv_nlkk_deproj'+dep+'_SENS'+sens+'_fsky_'+fsky+'_iterOn.csv')
            Apr17Off = np.loadtxt('output/Apr17_mv_nlkk_deproj'+dep+'_SENS'+sens+'_fsky_'+fsky+'_iterOff.csv')

            plt.plot(Apr17On[:,0],Apr17On[:,1]/Apr1[:,1]-1.,label='Apr17On/Apr1 - 1')
            plt.plot(Apr17Off[:,0],Apr17Off[:,1]/Apr1[:,1]-1.,label='Apr17Off/Apr1 - 1')
            #ErminiaEE = np.loadtxt('tests/Erminia-EE/Nell_comb_LAT_SENS'+sens+'_fsky'+fsky+'.txt')
            #CollinEE = np.loadtxt('tests/EE-BB/SOV3_pol_default1-4-2_noisecurves_deproj'+dep+'_SENS'+sens+'_mask_'+fsky+'_ell_EE_BB.txt')
            #plt.loglog(ErminiaEE[:,0],ErminiaEE[:,2],label='Erminia')
            #plt.loglog(CollinEE[:,0],CollinEE[:,1],label='Collin')
            plt.xlabel('$L$',fontsize=20)
            plt.ylabel('$N_L$',fontsize=20)
            plt.legend()
            plt.show()
            plt.close()
#plt.savefig('tests/Mar31_nlKK_TT_compare.png')
'''
for dep in ['0','1','2','3']:
    plt.figure(figsize=(10,8))
    c = color.next()
    Apr1 = np.loadtxt('output/Apr1_mv_AdvACT_nlkk_deproj'+dep+'_fsky_16000.csv')
    Apr17 = np.loadtxt('output/Apr17_mv_AdvACT_nlkk_deproj'+dep+'_fsky_16000_iterOn.csv')
    plt.loglog(Apr1[:,0],Apr1[:,1],label='Apr1')
    plt.loglog(Apr17[:,0],Apr17[:,1],label='Apr17')
    #plt.plot(Apr17[:,0],Apr17[:,1]/Apr1[:,1]-1.,label='Apr17/Apr1 - 1')
    plt.xlabel('$L$',fontsize=20)
    plt.ylabel('$N_L$',fontsize=20)
    plt.legend()
    plt.show()
    plt.close()                   
