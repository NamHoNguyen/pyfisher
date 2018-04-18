import numpy as np

combs = ['TT','TE','EE','TB','EB','mv']
ell,Nlkk = np.loadtxt('output/Apr16_TT_nlkk_deproj0_SENS2_fsky_04000.csv',unpack=True)
Nlkk = []
Nlkk.append(ell)
for comb in combs:
    noise = np.loadtxt('output/Apr16_'+comb+'_nlkk_deproj0_SENS2_fsky_04000.csv')
    Nlkk.append(noise[:,1])
np.savetxt('output/Apr16_nlkk_deproj0_SENS2_fsky_04000.csv',np.array(Nlkk).T)
    
