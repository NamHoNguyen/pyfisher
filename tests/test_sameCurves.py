import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import itertools
import matplotlib as mpl
mpl.rcParams.update({'font.family':'serif'})
mpl.rcParams.update({'mathtext.fontset':'cm'})
mpl.rcParams.update({'font.size': 18})
#mpl.rcParams['lines.linewidth'] = 3


i = 0
color = itertools.cycle(['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'])

June7 = np.loadtxt('output/June7_newoptimal_vhhAcc_unlensed_scalar_fCls.csv',delimiter=',')
May9 = np.loadtxt('output/May9_highAcc_unlensed_scalar_fCls.csv',delimiter=',')
ellmax = min(len(June7[:,0]),len(May9[:,0]))
ell = range(ellmax)

plt.semilogx(ell,May9[:ellmax,i]/June7[:ellmax,i],label='ratio')
plt.title('fiducial')
plt.xlim([0,5000])
plt.show()
plt.clf()


for param in 'H0,ombh2,omch2,tau,As,ns,mnu,nnu,w'.split(','):
    June7 = np.loadtxt('output/June7_newoptimal_vhhAcc_unlensed_scalar_dCls_'+param+'.csv',delimiter=',')
    May9 = np.loadtxt('output/May9_highAcc_unlensed_scalar_dCls_'+param+'.csv',delimiter=',')
    ellmax = min(len(June7[:,0]),len(May9[:,0]))
    ell = range(ellmax)
    
    plt.semilogx(ell,May9[:ellmax,i]/June7[:ellmax,i],label='ratio')
    #plt.semilogx(ell,May9[:ellmax,i],label='May9')
    #plt.semilogx(ell,June7[:ellmax,i],label='June7')
    #print max(May9[:ellmax,i]/June7[:ellmax,i])
    plt.xlabel('$\ell$',fontsize=20)
    #plt.ylabel('ratio',fontsize=20)
    plt.title(param)
    plt.legend()
    plt.xlim([0,5000])
    plt.show()
    plt.clf()
#plt.savefig('tests/Mar31_nlKK_TT_compare.png')
