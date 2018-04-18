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

#Anthony = np.loadtxt('tests/Anthony/SOV3_Nlpp_default1-4-2_deproj0_SENS2_mask_04000_effort100.dat')
Anthony = np.loadtxt('tests/Anthony/SOV3_Nlpp_default1-4-2_deproj0_SENS2_mask_04000_effort100_lmaxT3000.dat')
Anthony[:,1:] = Anthony[:,1:]*(2.*np.pi/4.)

mine = np.loadtxt('output/Apr16_nlkk_deproj0_SENS2_fsky_04000.csv')

myMVdelens = np.loadtxt('tests/Apr1_mv_L_kk/Apr1_mv_nlkk_deproj0_SENS2_fsky_04000.csv')
myET = np.loadtxt('output/Apr16_ET_nlkk_deproj0_SENS2_fsky_04000.csv')


CollinTT = np.loadtxt('tests/KK-TT/SOV3_T_default1-4-2_noisecurves_deproj0_SENS2_mask_04000_L_kk.txt')
CollinEB = np.loadtxt('tests/KK-EB/SOV3_pol_default1-4-2_noisecurves_deproj0_SENS2_mask_04000_L_kk.txt')

# TT position is 1, EB is 5
pos = 1
c = color.next()
plt.loglog(Anthony[:,0],Anthony[:,pos],c,label="Anthony TT")
plt.loglog(mine[:,0],mine[:,pos],c+'--',label="Nam TT")
plt.loglog(CollinTT[:,0],CollinTT[:,1],c+'-.',label="Collin TT")

pos = 5
c = color.next()
plt.loglog(Anthony[:,0],Anthony[:,pos],c,label="Anthony EB")
plt.loglog(mine[:,0],mine[:,pos],c+'--',label="Nam EB")
plt.loglog(CollinEB[:,0],CollinEB[:,1],c+'-.',label="Collin EB")

plt.xlabel('$L$')
plt.ylabel('$N_{L}^{\kappa\kappa}$')
plt.legend()
plt.show()

plt.clf()


labels = ['TT','TE','EE','TB','EB','MV']
for i in range(len(labels)):
    c = color.next()
    if labels[i]=='MV':
        plt.loglog(Anthony[:,0],Anthony[:,i+1],c,label="Anthony "+labels[i])
        plt.loglog(mine[:,0],mine[:,i+1],c+'--',label="Nam "+labels[i])
    else:
        plt.loglog(Anthony[:,0],Anthony[:,i+1],c,label=labels[i])
        plt.loglog(mine[:,0],mine[:,i+1],c+'--')

#plt.loglog(myMVdelens[:,0],myMVdelens[:,1],c+':',label='My MV delens')
#c = color.next()
plt.loglog(myET[:,0],myET[:,1],'C3:',label='Nam ET')

'''
TEfunc = interp1d(ell,TE,bounds_error=False,fill_value=np.inf)
myTEfunc = interp1d(myell,myTE,bounds_error=False,fill_value=np.inf)
myETfunc = interp1d(myell,myET,bounds_error=False,fill_value=np.inf)
ellmin = max(ell[0],myell[0])
ellmax = min(ell[-1],myell[-1])
ellrange = np.arange(ellmin,ellmax,1)

print myTEfunc(ellrange)/TEfunc(ellrange),myETfunc(ellrange)/TEfunc(ellrange)
'''

plt.xlabel('$L$')
plt.ylabel('$N_{L}^{\kappa\kappa}$')
plt.legend(loc='upper left')
plt.show()
#plt.clf()
#plt.savefig('tests/Mar31_nlKK_TT_compare.png')

