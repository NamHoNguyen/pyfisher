import numpy as np
import matplotlib.pyplot as plt

noiseList = np.arange(0.25,6,0.5)

TCMB = 2.7255e6

BB = np.loadtxt('output/Feb17_noatm_iter_krange_5_3000_beam_1arcmin_clbb_noise_0.25.csv')
plt.plot(BB[:,0],np.sqrt(BB[:,1])*TCMB*180.*60./np.pi,'k--',label='original')

for noise in noiseList[::-1]:
    BB = np.loadtxt('output/Feb17_noatm_iter_krange_5_3000_beam_1arcmin_clbb_noise_'+str(noise)+'.csv')
    plt.semilogx(BB[:,0],np.sqrt(BB[:,2])*TCMB*180.*60./np.pi,label=str(noise)+' uK-arcmin')

plt.xlabel('$\ell$')
plt.ylabel('$\\sqrt{C_{\ell}^{BB}}$ [uK-arcmin]')
plt.xlim([1,1e5])
plt.ylim([0,7])
plt.legend()
plt.savefig('tests/Feb17_delensing_checkBBdiff.png')
#plt.show()
    
