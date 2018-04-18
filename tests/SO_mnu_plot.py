import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib as mpl
mpl.rcParams.update({'font.family':'serif'})
mpl.rcParams.update({'mathtext.fontset':'cm'})
mpl.rcParams.update({'font.size': 18})
mpl.rcParams['lines.linewidth'] = 3

color = itertools.cycle(['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'])
ls=itertools.cycle(['-','--',':'])
taus = [0.01,0.005,0.002]
fskys = [0.1,0.2,0.4]
noises = ['Threshold','Baseline','Goal']


#prefix = 'output/Feb23_deproj0'
prefix = 'output/Apr17_deproj1'
#prefix = 'output/Mar8_deproj0_polOnly'

fig = plt.figure(figsize=(10,8))

ACT = np.loadtxt('output/Apr17_mv_AdvACT_tau_deproj_mnu.csv')
deproj = 1
fskyACT = 0.4

m = 0
for tau in taus:
    c = color.next()
    mnus = np.loadtxt(prefix+'_tau_'+str(tau)+'_mnu.csv')
    for i in range(len(noises)):
        l = ls.next()
        if tau == taus[0]:
            plt.plot(fskys,mnus[:,i],c+l+'o',label='$\\sigma(\\tau)=$'+str(tau)+', '+noises[i])
        else:
            if i == 0:
                plt.plot(fskys,mnus[:,i],c+l+'o',label='$\\sigma(\\tau)=$'+str(tau))
            else:
                plt.plot(fskys,mnus[:,i],c+l+'o')
    if m == 0:
        plt.plot(fskyACT,ACT[m,deproj],c+'x',label='$\\sigma(\\tau)=$'+str(tau)+', AdvACT',markersize=18)
    else:
        plt.plot(fskyACT,ACT[m,deproj],c+'x',markersize=18)
    m += 1
plt.xlabel('$f_{sky}$',fontsize=20)
plt.ylabel('$\\sigma(\Sigma m_{\\nu})$',fontsize=20)
plt.ylim([15,55])
plt.legend()
#plt.show()
plt.savefig('output/Apr17_deproj1_mnu.png')    
plt.clf()

# Lensing S/N plot
ls=itertools.cycle(['-','--',':'])
color = itertools.cycle(['C0', 'C1', 'C2']) #, 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'])
#sns1 = np.loadtxt('output/Feb23_deproj0_tau_0.01_sn.csv')
#sns2 = np.loadtxt('output/Mar8_deproj0_polOnly_tau_0.01_sn.csv')
sns1 = np.loadtxt('output/Apr17_deproj0_tau_0.01_sn.csv')
sns2 = np.loadtxt('output/Apr17_polOnly_deproj0_tau_0.01_sn.csv')
sns3 = np.loadtxt('output/Apr17_deproj1_tau_0.01_sn.csv')
for i in range(len(noises)):
    #c = color.next()
    l = ls.next()
    if i == 0:
        c = color.next()
        l1, =plt.plot(fskys,sns1[:,i],c+l+'o',label=noises[i]+' - deproj0, mv')
        c = color.next()
        l2, = plt.plot(fskys,sns2[:,i],c+l+'o',label=noises[i]+' - deproj0, pol only') #,alpha=0.3)
        c = color.next()
        #l = ls.next()
        l3, = plt.plot(fskys,sns3[:,i],c+l+'o',label=noises[i]+' - deproj1, mv')
    else:
        c = color.next()
        l1, =plt.plot(fskys,sns1[:,i],c+l+'o',label=noises[i])
        c = color.next()
        l2, = plt.plot(fskys,sns2[:,i],c+l+'o',alpha=0.3)
        c = color.next()
        #l = ls.next()
        l3, = plt.plot(fskys,sns3[:,i],c+l+'o')

plt.xlabel('$f_{sky}$',fontsize=20)
plt.ylabel('Lensing S/N',fontsize=20)
#plt.ylim([15,45])
plt.legend()
plt.savefig('output/Apr17_deproj0_deproj1_sn.png')    
#plt.savefig('output/Mar9_deproj0_sn.png')    


