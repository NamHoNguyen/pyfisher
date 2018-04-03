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
for dep in ['0']:
    TT = np.loadtxt('output/Apr1_TT_AdvACT_nlkk_deproj'+dep+'_fsky_16000.csv')
    EB = np.loadtxt('output/Apr1_EB_AdvACT_nlkk_deproj'+dep+'_fsky_16000.csv')
    mv = np.loadtxt('output/Apr1_mv_AdvACT_nlkk_deproj'+dep+'_fsky_16000.csv')

    c = color.next()
    plt.loglog(TT[:,0],TT[:,1],c+':',label='TT')
    plt.loglog(EB[:,0],EB[:,1],c+'--',label='EB')
    plt.loglog(mv[:,0],mv[:,1],c+'-',label='mv')
plt.xlabel('$L$',fontsize=20)
plt.ylabel('$N_L^{\kappa\kappa}$',fontsize=20)
plt.title('deproj0')
plt.legend()
#plt.show()
plt.savefig('tests/Apr1_AdvACT_nlkk.png')
