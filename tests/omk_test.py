import numpy as np
import matplotlib.pyplot as plt
import sys
i = 4
lmin = 20
lmax = 5000
'''
params = ['As','H0','ombh2','omch2','ns','tau','mnu','nnu']
for param in params:  
    old = np.loadtxt('output/June7_newoptimal_vhhAcc_unlensed_scalar_dCls_'+param+'.csv',delimiter=',')
    new = np.loadtxt('output/Mar9_highAcc__unlensed_scalar_dCls_'+param+'.csv',delimiter=',')

    plt.figure(1)
    plt.subplot(121)
    plt.plot(range(lmin,lmax),old[lmin:lmax,i],label='old '+str(i))
    plt.plot(range(lmin,lmax),new[lmin:lmax,i],label='new '+str(i))
    plt.xscale('log')
    plt.legend()

    plt.subplot(122)
    plt.plot(range(lmin,lmax),(new[lmin:lmax,i]-old[lmin:lmax,i])/old[lmin:lmax,i],label='frac diff-col='+str(i))
    plt.plot(range(lmin,lmax),(new[lmin:lmax,i]-old[lmin:lmax,i])/new[lmin:lmax,i],label='frac diff-col='+str(i))
    plt.title(param)
    plt.legend()
    plt.show()
    plt.clf()
'''
#low = np.loadtxt('output/Mar9_lowAcc_unlensed_scalar_dCls_omk.csv',delimiter=',')
#high = np.loadtxt('output/Mar9_highAcc_unlensed_scalar_dCls_omk.csv',delimiter=',')
low = np.loadtxt('output/Mar9_highAcc_unlensed_scalar_fCls.csv',delimiter=',')
high = np.loadtxt('output/Mar9_highAcc__unlensed_scalar_fCls.csv',delimiter=',')
print len(low),len(high)
for i in range(6):
    plt.figure(1)
    plt.subplot(121)
    plt.plot(range(lmin,lmax),low[lmin:lmax,i],label='low '+str(i))
    plt.plot(range(lmin,lmax),high[lmin:lmax,i],label='high '+str(i))
    plt.xscale('log')
    plt.legend()
    
    plt.subplot(122)
    plt.plot(range(lmin,lmax),(low[lmin:lmax,i]-high[lmin:lmax,i])/high[lmin:lmax,i],label='frac diff-col='+str(i))
    plt.plot(range(lmin,lmax),(low[lmin:lmax,i]-high[lmin:lmax,i])/low[lmin:lmax,i],label='frac diff-col='+str(i))
    plt.legend()
    plt.show()
    plt.clf()
