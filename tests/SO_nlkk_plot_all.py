import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib as mpl
mpl.rcParams.update({'font.family':'serif'})
mpl.rcParams.update({'mathtext.fontset':'cm'})
#mpl.rcParams['lines.linewidth'] = 3

#color=itertools.cycle(['b','r','g','c','m','y','k'])
color = itertools.cycle(['C0', 'C1', 'C2']) #, 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'])
ls = itertools.cycle(['-','--',':']) #,'-.'])
depList = ['0','1','2','3']
fskyList = ['04000','08000','16000']
sensList = ['0','1','2']
iterList = ['On','Off']

for iteration in iterList:
    plt.figure(figsize=(20,10))
    i = 1
    for depNow in depList:
        plt.subplot(2,2,i)
        for fskyNow in fskyList:
            c = color.next()
            for sensNow in sensList:
                l = ls.next()
                Nls = np.loadtxt('output/Apr17_mv_nlkk_deproj'+depNow+'_SENS'+sensNow+'_fsky_'+fskyNow+'_iter'+iteration+'.csv')
                l1, = plt.loglog(Nls[:,0],Nls[:,1],c+l,label='SENS'+sensNow+'_'+fskyNow)
                #Nls = np.loadtxt('output/Apr17_mv_nlkk_deproj'+depNow+'_SENS'+sensNow+'_fsky_'+fskyNow+'_iterOff.csv')
                #l1, = plt.semilogy(Nls[::100,0],Nls[::100,1],c+l+'o',alpha=0.5,markersize=5)
        plt.xlabel('$L$')
        plt.ylabel('$N_L^{\kappa\kappa}$')
        plt.title('deproj'+depNow+'_iter'+iteration)
        plt.legend()
        plt.ylim([1e-8,1e-5])
        i+=1
    #plt.legend(handles=[l1])
    plt.savefig('tests/Apr17_mv_nlkk_iter'+iteration+'.png')
    plt.close()
    #plt.show()

ls = itertools.cycle(['-','--'])
color = itertools.cycle(['C0', 'C1', 'C2', 'C3']) #, 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'])
plt.figure(figsize=(20,8))
plt.subplot(1,2,1)
for depNow in depList:
    c = color.next()
    for iteration in iterList:
        l = ls.next()

        Nls = np.loadtxt('output/Apr17_mv_AdvACT_nlkk_deproj'+depNow+'_fsky_16000_iter'+iteration+'.csv')
        if depNow == depList[0]:
            plt.loglog(Nls[:,0],Nls[:,1],c+l,label='deproj'+depNow+' iter'+iteration)
        else:
            if iteration == 'On':
                plt.loglog(Nls[:,0],Nls[:,1],c+l,label='deproj'+depNow)
            else:
                plt.loglog(Nls[:,0],Nls[:,1],c+l)
plt.xlabel('$L$')
plt.ylabel('$N_L^{\kappa\kappa}$')                
plt.legend()

plt.subplot(1,2,2)
for depNow in depList:
    c = color.next()
    NlsOn = np.loadtxt('output/Apr17_mv_AdvACT_nlkk_deproj'+depNow+'_fsky_16000_iterOn.csv')
    NlsOff = np.loadtxt('output/Apr17_mv_AdvACT_nlkk_deproj'+depNow+'_fsky_16000_iterOff.csv')
    plt.semilogx(NlsOn[:,0],NlsOn[:,1]/NlsOff[:,1],label='deproj'+depNow)
plt.xlabel('$L$')
plt.ylabel('iterOn/iterOff')
plt.legend()
plt.savefig('tests/Apr17_mv_AdvACT_nlkk.png')    
#plt.show()
