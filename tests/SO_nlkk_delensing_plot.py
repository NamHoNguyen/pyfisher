import numpy as np
import matplotlib.pyplot as plt
import itertools
import matplotlib as mpl
mpl.rcParams.update({'font.family':'serif'})
mpl.rcParams.update({'mathtext.fontset':'cm'})
#mpl.rcParams.update({'mathtext.fontsize':18})
mpl.rcParams.update({'font.size': 18})
mpl.rcParams['lines.linewidth'] = 3

fig = plt.figure(figsize=(10,8))

color = itertools.cycle(['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'])
ls=itertools.cycle([':','--','-'])

fskyNow = '04000'
timeList = [100,50,25]
noiseList = ['Threshold','Baseline','Goal']
#noiseList = ['SENS0','SENS1','SENS2']

#mv = np.loadtxt('output/Feb23_mv_fsky_0.1_time_sens_delensingEff.csv')
#polOnly = np.loadtxt('output/Mar8_polOnly_fsky_0.1_time_sens_delensingEff.csv')
#mv = np.loadtxt('output/Apr1_mv_time_sens_delensingEff.csv')
#polOnly = np.loadtxt('output/Apr1_polOnly_time_sens_delensingEff.csv')
mv = np.loadtxt('output/Apr17_mv_time_sens_iterOn_delensingEff.csv')
polOnly = np.loadtxt('output/Apr17_polOnly_time_sens_iterOn_delensingEff.csv')
'''
i = 0
for noiseNow in noiseList:
    c = color.next()
    plt.plot(timeList,mv[:,i],c+'-o',label=noiseNow+' mv')
    plt.plot(timeList,polOnly[:,i],c+'--o',label=noiseNow +' mv (pol only)')
    i+=1
plt.xlabel('Percentage of time')
plt.ylabel('Delensing efficiency (%)')
plt.title('$f_{sky}$=0.1')
plt.xlim([15,110])
plt.legend()
#plt.show()
plt.savefig('tests/Apr17_delensingEff_time.png')
'''
i = 0
for noiseNow in noiseList:
    c = color.next()
    if noiseNow == noiseList[0]:
        plt.plot(timeList,100.-mv[:,i],c+'-o',label=noiseNow+' - mv')
        plt.plot(timeList,100.-polOnly[:,i],c+'--o',label=noiseNow +' - pol only')
    else:
        plt.plot(timeList,100.-mv[:,i],c+'-o',label=noiseNow)
        plt.plot(timeList,100.-polOnly[:,i],c+'--o')
    i+=1
plt.xlabel('Percentage of time',fontsize=20)
plt.ylabel('$A_{\\rm lens}$',fontsize=25)
plt.title('$f_{sky}=0.1$',fontsize=25)
plt.xlim([15,110])
plt.legend()
#plt.show()
plt.savefig('tests/Apr17_Alens_time.png')

