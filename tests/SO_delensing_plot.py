import numpy as np
import matplotlib.pyplot as plt
import itertools
color=itertools.cycle(['b','r','g','c','m','y','k'])

Bnoise_max = 5.5/5.3
Bnoise_scale = 5.86/5.3
quadB = np.loadtxt('output/Feb21_noatm_quad_beam_1arcmin_lensingB_delensB_eff.csv')
iterB = np.loadtxt('output/Feb21_noatm_iter_beam_1arcmin_lensingB_delensB_eff.csv')
quadBnoise = np.loadtxt('output/quadratic_delensing.csv')
iterBnoise = np.loadtxt('output/iterative_delensing.csv')

#plt.plot(quadB[:,0],quadB[:,0],'k')

c=color.next()
#plt.plot(quadB[:,0],5.3+0.*quadB[:,0],c+'-',label="CMB-S4 no delens")
#plt.plot(quadB[:,0],quadB[:,1]*Bnoise_scale,c+'--',label="Mat's no delens") # - quadratic")

origBB = (5.3*Bnoise_max+0.*quadBnoise[:,0])**2
c=color.next()
plt.plot(quadBnoise[:,0],(origBB-(quadBnoise[:,1]*Bnoise_scale)**2)/origBB*100.,c+'-',label="CMB-S4 SB quad delens")
plt.plot(quadB[:,0],quadB[:,3],c+'--',label="Mat's quad delens 1 arcmin") # - explicit")

origBB = (5.3*Bnoise_max+0.*iterBnoise[:,0])**2
c=color.next()
plt.plot(iterBnoise[:,0],(origBB-(iterBnoise[:,1]*Bnoise_scale)**2)/origBB*100.,c+'-',label="CMB-S4 SB iter delens")
plt.plot(iterB[:,0],iterB[:,3],c+'--',label="Mat's iter delens 1 arcmin") # - explicit")

#plt.xlim([0,7])
#plt.ylim([0,7])
plt.xlabel('Noise [uK-arcmin]')
plt.ylabel('Lensing B-mode Noise [uK-arcmin]')
plt.legend()
plt.show()
#plt.savefig('tests/Feb21_delensing_checkEfficiencyFormula.png')
