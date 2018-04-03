import numpy as np
import matplotlib.pyplot as plt
import itertools
color=itertools.cycle(['b','r','g','c','m','y','k'])
ls=itertools.cycle(['-','--',':'])
#taus = [0.06,0.01,0.005,0.002]
taus = [0.01,0.005,0.002]
fskys = [0.1,0.2,0.4]
noises = ['Threshold','Baseline','Goal']


#prefix = 'output/Feb23_deproj0'
prefix = 'output/Apr1_deproj0'
#prefix = 'output/Mar8_deproj0_polOnly'

for tau in taus:
    c = color.next()
    mnus = np.loadtxt(prefix+'_tau_'+str(tau)+'_mnu.csv')
    for i in range(len(noises)):
        l = ls.next()
        plt.plot(fskys,mnus[:,i],c+l+'o',label='$\\sigma(\\tau)=$'+str(tau)+', '+noises[i])
plt.xlabel('fsky')
plt.ylabel('$\\sigma(mnu)$')
plt.ylim([15,45])
plt.legend()
plt.savefig(prefix+'_mnu.png')    

plt.clf()
'''
# Lensing S/N plot
ls=itertools.cycle(['-','--'])
#sns1 = np.loadtxt('output/Feb23_deproj0_tau_0.01_sn.csv')
#sns2 = np.loadtxt('output/Mar8_deproj0_polOnly_tau_0.01_sn.csv')
sns1 = np.loadtxt('output/Apr1_deproj1_tau_0.01_sn.csv')
sns2 = np.loadtxt('output/Apr1_polOnly_deproj1_tau_0.01_sn.csv')
for i in range(len(noises)):
    c = color.next()
    l = ls.next()
    plt.plot(fskys,sns1[:,i],c+l+'o',label=noises[i]+' mv')
    l = ls.next()
    plt.plot(fskys,sns2[:,i],c+l+'o',label=noises[i]+' mv (pol only)')

plt.xlabel('fsky')
plt.ylabel('Lensing S/N')
#plt.ylim([15,45])
plt.legend()
plt.savefig('output/Apr1_deproj1_sn.png')    
#plt.savefig('output/Mar9_deproj0_sn.png')    
'''
