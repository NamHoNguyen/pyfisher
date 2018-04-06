import sys
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

ell,TT,TE,EE,TB,EB,MV = np.loadtxt('tests/Anthony/SOV3_Nlpp_default1-4-2_deproj0_SENS2_mask_04000_effort100.dat',unpack=True)
Anthony = [TT,TE,EE,TB,EB,MV]

myell,myMVdelens = np.loadtxt('tests/Apr1_mv_L_kk/Apr1_mv_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
myell,myMV = np.loadtxt('output/Apr5_mv_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
myell,myTT = np.loadtxt('output/Apr5_TT_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
myell,myTTAnthony = np.loadtxt('output/Apr5_TT_AnthonyCosmo_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
myell,myTE = np.loadtxt('output/Apr5_TE_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
myell,myEE = np.loadtxt('output/Apr5_EE_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
myell,myTB = np.loadtxt('output/Apr5_TB_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
myell,myEB = np.loadtxt('output/Apr5_EB_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
myell,myEBAnthony = np.loadtxt('output/Apr5_EB_AnthonyCosmo_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
mine = [myTT,myTE,myEE,myTB,myEB,myMV]

CollinTT = np.loadtxt('tests/KK-TT/SOV3_T_default1-4-2_noisecurves_deproj0_SENS2_mask_04000_L_kk.txt')
CollinEB = np.loadtxt('tests/KK-EB/SOV3_pol_default1-4-2_noisecurves_deproj0_SENS2_mask_04000_L_kk.txt')

c = color.next()
plt.loglog(ell,TT,c,label="Anthony's TT")
plt.loglog(myell,myTT,c+'--',label="My TT - quicklens Cosmology")
plt.loglog(myell,myTTAnthony,c+':',label="My TT - Anthony's Comoslogy")
c = color.next()
plt.loglog(CollinTT[:,0],CollinTT[:,1],c+'-.',label="Collin's TT")

c = color.next()
plt.loglog(ell,EB,c,label="Anthony's EB")
plt.loglog(myell,myEB,c+'--',label="My EB - quicklens Cosmology")
plt.loglog(myell,myEBAnthony,c+':',label="My EB - Anthony's Comoslogy")
c = color.next()
plt.loglog(CollinEB[:,0],CollinEB[:,1],c+'-.',label="Collin's EB")

plt.xlabel('$L$')
plt.ylabel('$N_{L}^{\kappa\kappa}$')
plt.legend()
plt.show()

plt.clf()

labels = ['TT','TE','EE','TB','EB','MV']
for i in range(len(labels)):
    c = color.next()
    #if labels[i] == 'MV':
    if False:
        plt.loglog(ell,Anthony[i],c,label="Anthony's "+labels[i])
        plt.loglog(myell,mine[i],c+'--',label="My "+labels[i]+" - quicklens Cosmology")
    else:
        plt.loglog(ell,Anthony[i],c,label=labels[i])
        plt.loglog(myell,mine[i],c+'--')
#plt.loglog(myell,myMVdelens,c+':',label='My MV delens')

plt.xlabel('$L$')
plt.ylabel('$N_{L}^{\kappa\kappa}$')
plt.legend()
plt.show()
#plt.clf()
#plt.savefig('tests/Mar31_nlKK_TT_compare.png')
