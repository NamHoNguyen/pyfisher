import numpy as np
import matplotlib.pyplot as plt
import itertools
color=itertools.cycle(['b','r','g','c','m','y','k'])
ls=itertools.cycle([':','--','-'])

fskyNow = '04000'
timeList = [100,50,25]
noiseList = ['Threshold','Baseline','Goal']
#noiseList = ['SENS0','SENS1','SENS2']

mv = np.loadtxt('output/Feb23_mv_fsky_0.1_time_sens_delensingEff.csv')
polOnly = np.loadtxt('output/Mar8_polOnly_fsky_0.1_time_sens_delensingEff.csv')

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
plt.savefig('tests/Mar8_delensingEff_time.png')
