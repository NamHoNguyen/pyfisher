import numpy as np
import matplotlib.pyplot as plt
import itertools

color=itertools.cycle(['b','r','g','c','m','y','k'])
fskyList = ['04000','08000','16000']
noiseList = ['SENS1'] #,'SENS1','SENS2']

for fskyNow in fskyList:
    for noiseNow in noiseList:
        c = color.next()
        Nl1 = np.loadtxt('tests/KK/SOV3_T_default1-4-2_noisecurves_deproj0_'+noiseNow+'_mask_'+fskyNow+'_L_kk.txt')
        #Nl2 = np.loadtxt('output/Feb23_TT_nlkk_deproj0_'+noiseNow+'_fksy_'+fskyNow+'.csv')
        Nl2 = np.loadtxt('output/Mar8_polOnly_nlkk_deproj0_'+noiseNow+'_fsky_'+fskyNow+'.csv')
        Nl3 = np.loadtxt('output/Feb23_mv_nlkk_deproj0_'+noiseNow+'_fsky_'+fskyNow+'.csv')
        l1, = plt.semilogy(Nl1[:,0],Nl1[:,1],c,label="Collin's kk")
        #l2, = plt.semilogy(Nl2[:,0],Nl2[:,1],c+'--',label="TT estimator")
        l2, = plt.semilogy(Nl2[:,0],Nl2[:,1],c+'--',label="mv (pol only)")
        l3, = plt.semilogy(Nl3[:,0],Nl3[:,1],c+':',label="mv estimator with iterative physics")
plt.xlabel('$L$')
plt.ylabel('$N_L^{\kappa\kappa}$')
plt.title('Baseline with 3 sky coverages')
plt.legend(handles=[l1,l2,l3])
plt.savefig('tests/Mar8_nlkk.png')
#plt.show()
