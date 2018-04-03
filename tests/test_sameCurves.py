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
for dep in ['0','1','2','3']:
    ell,EE,BB = np.loadtxt('tests/AdvACT/AdvACT_pol_default_Nseasons4.0_NLFyrs2.0_noisecurves_deproj0_mask_16000_ell_EE_BB.txt',unpack=True)
    c = color.next()
    plt.plot(ell,EE/BB,label='ratio')
    print max(EE/BB)
    plt.xlabel('$\ell$',fontsize=20)
    plt.ylabel('$N_{\ell}^{EE}/N_{\ell}^{BB}$',fontsize=20)
    plt.legend()
    plt.show()
    plt.clf()
#plt.savefig('tests/Mar31_nlKK_TT_compare.png')
