import numpy as np
import matplotlib.pyplot as plt
import itertools
color=itertools.cycle(['b','r','g','c','m','y','k'])

Bnoise_max = 5.5
Bnoise_scale = 1. #5.3/5.86
quadB = np.loadtxt('output/Feb21_noatm_quad_beam_1arcmin_lensingB_delensB_eff.csv')
iterB = np.loadtxt('output/Feb21_noatm_iter_beam_1arcmin_lensingB_delensB_eff.csv')
quadBP = np.loadtxt('output/Feb21_noatm_quad_beam_1arcmin_PlanckCosmo_lensingB_delensB_eff.csv')
iterBP = np.loadtxt('output/Feb21_noatm_iter_beam_1arcmin_PlanckCosmo_lensingB_delensB_eff.csv')
quadBT = np.loadtxt('output/Feb22_noatm_quad_beam_1arcmin_TestCosmo_lensingB_delensB_eff.csv')
iterBT = np.loadtxt('output/Feb22_noatm_iter_beam_1arcmin_TestCosmo_lensingB_delensB_eff.csv')
quadBnoise = np.loadtxt('output/quadratic_delensing.csv')
iterBnoise = np.loadtxt('output/iterative_delensing.csv')

c=color.next()
plt.plot(quadB[:,0],quadB[:,3],c+'-',label="Mat's quad")
plt.plot(quadBP[:,0],quadBP[:,3],c+'--',label="Mat's quad Planck")
plt.plot(quadBT[:,0],quadBT[:,3],c+':',label="Mat's quad Test")

c=color.next()
plt.plot(iterB[:,0],iterB[:,3],c+'-',label="Mat's iter")
plt.plot(iterBP[:,0],iterBP[:,3],c+'--',label="Mat's iter Planck")
plt.plot(iterBT[:,0],iterBT[:,3],c+':',label="Mat's iter Test")

plt.xlabel('Noise [uK-arcmin]')
plt.ylabel('Delensing efficiency (%)')

plt.legend()
plt.savefig('tests/Feb28_delensing_efficiency.png')
plt.clf()

#---------------------------------------------#
color=itertools.cycle(['b','r','g','c','m','y','k'])
plt.plot(quadB[:,0],quadB[:,0],'k')

c=color.next()
plt.plot(quadB[:,0],5.3+0.*quadB[:,0],c+'-',label="CMB-S4 no delens")
#plt.plot(quadB[:,0],quadB[:,1]*Bnoise_scale,c+'--',label="Mat's no delens") # - quadratic")
plt.plot(quadBP[:,0],quadBP[:,1]*Bnoise_scale,c+'--',label="Mat's no delens Planck") # - quadratic")
#plt.plot(quadBT[:,0],quadBT[:,1]*Bnoise_scale,c+':',label="Mat's no delens Test") # - quadratic")

c=color.next()
plt.plot(quadBnoise[:,0],quadBnoise[:,1],c+'-',label="CMB-S4 SB quad delens")
#plt.plot(quadB[:,0],quadB[:,2]*Bnoise_scale,c+'--',label="Mat's quad delens 1 arcmin") # - explicit")
plt.plot(quadBP[:,0],quadBP[:,2]*Bnoise_scale,c+'--',label="Mat's quad delens 1 arcmin Planck") # - explicit")
#plt.plot(quadBT[:,0],quadBT[:,2]*Bnoise_scale,c+':',label="Mat's quad delens 1 arcmin Test") # - explicit")
#plt.plot(quadB[:,0],np.sqrt((1.-quadB[:,3]/100.))*Bnoise_max,c+':',label="Mat's quad delens 1 arcmin - sqrt(e)")

c=color.next()
plt.plot(iterBnoise[:,0],iterBnoise[:,1],c+'-',label="CMB-S4 SB iter delens")
#plt.plot(iterB[:,0],iterB[:,2]*Bnoise_scale,c+'--',label="Mat's iter delens 1 arcmin") # - explicit")
plt.plot(iterBP[:,0],iterBP[:,2]*Bnoise_scale,c+'--',label="Mat's iter delens 1 arcmin Planck") # - explicit")
#plt.plot(iterBT[:,0],iterBT[:,2]*Bnoise_scale,c+':',label="Mat's iter delens 1 arcmin Test") # - explicit")
#plt.plot(iterB[:,0],np.sqrt((1.-iterB[:,3]/100.))*Bnoise_max,c+':',label="Mat's iter delens 1 arcmin - sqrt(e)")

plt.xlim([0,7])
plt.ylim([0,7])
plt.xlabel('Noise [uK-arcmin]')
plt.ylabel('Lensing B-mode Noise [uK-arcmin]')


plt.legend()
#plt.show()
plt.savefig('tests/Feb28_delensing_checkEfficiencyFormula.png')

