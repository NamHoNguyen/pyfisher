import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib as mpl
mpl.rcParams.update({'font.family':'serif'})
mpl.rcParams.update({'mathtext.fontset':'cm'})
#mpl.rcParams['lines.linewidth'] = 3
import sys

#color=itertools.cycle(['b','r','g','c','m','y','k'])
color = itertools.cycle(['C0', 'C1', 'C2']) #, 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'])
ls = itertools.cycle(['-','--',':']) #,'-.'])
sensLabel = {'1':'Baseline','2':'Goal'}
depLabel = {'0':'Standard ILC (no deproj.)','3':'tSZ+CIB and dust+synch. deprojected'}
cambRoot = '../quicklens/quicklens/data/cl/planck_wp_highL/planck_lensing_wp_highL_bestFit_20130627'

elldd, cldd = np.loadtxt(cambRoot+"_lenspotentialCls.dat",unpack=True,usecols=[0,5])
clkk = 2.*np.pi*cldd/4.
plt.loglog(elldd,clkk,'k',label='Lensing Power')

# Only fsky = 0.4
fskyNow = '16000'

# Baseline/Goal, deproj0, mv
l = ls.next()
sensList = ['1','2']
depNow = '0'
for sensNow in sensList:
    c = color.next()
    Nls = np.loadtxt('output/Apr17_mv_nlkk_deproj'+depNow+'_SENS'+sensNow+'_fsky_'+fskyNow+'_iterOn.csv')
    plt.loglog(Nls[:,0],Nls[:,1],c+l,label=sensLabel[sensNow]+' / '+depLabel[depNow]+' / min-var.')

# Goal, deproj0, polOnly
l = ls.next()
sensNow = '2'
depNow = '0'
Nls = np.loadtxt('output/Apr17_polOnly_nlkk_deproj'+depNow+'_SENS'+sensNow+'_fsky_'+fskyNow+'_iterOn.csv')
plt.loglog(Nls[:,0],Nls[:,1],c+l,label=sensLabel[sensNow]+' / '+depLabel[depNow]+' / pol. only')

# Goal, deproj3, mv
l = ls.next()
sensNow = '2'
depNow = '3'
Nls = np.loadtxt('output/Apr17_mv_nlkk_deproj'+depNow+'_SENS'+sensNow+'_fsky_'+fskyNow+'_iterOn.csv')
plt.loglog(Nls[:,0],Nls[:,1],c+l,label=sensLabel[sensNow]+' / '+depLabel[depNow]+' / min-var.')

# Planck
c = color.next()
Nls = np.loadtxt('output/Planck_nlkk.dat')
plt.loglog(Nls[:,0],Nls[:,1],c,label='Planck')
#plt.loglog(Nls[:,0],Nls[:,2],c+'--',label='Planck - 3rd column')

plt.xlabel('$L$',fontsize=20)
plt.ylabel('$C_L^{\kappa\kappa}$',fontsize=20)
plt.title('$\kappa\kappa (f_{\\rm sky}=$'+str(float(fskyNow)/40000.)+'): SO LAT + Planck')
plt.legend(loc='lower right')
plt.xlim([20,3000])
plt.ylim([1e-9,1e-5])
plt.xscale('linear')
#plt.show()
plt.savefig('tests/Apr17_mv_nlkk.png')
