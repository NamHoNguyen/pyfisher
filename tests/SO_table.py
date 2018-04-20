import numpy as np

timeIndex = 2 # 0.25% effort on fsky = 0.1 corresponding to fsky = 0.4
depIndex = 0
tauIndex = 0 # 0.01
sensIndex = 1 # Baseline - SENS1
fskyIndex = 2 # fsky = 0.4 or 16000 sqdeg

print '\nprior on tau is 0.01, with DESI'
ACT_eff = np.loadtxt('output/Apr17_mv_AdvACT_dep_iterOn_delensingEff.csv')
ACT_mnu = np.loadtxt('output/Apr17_mv_AdvACT_tau_deproj_mnu.csv')
ACT_sn = np.loadtxt('output/Apr17_mv_AdvACT_tau_deproj_sn.csv') 
print '\t\t\t Alens','\t mnu','\t S/N'
print 'AdvACT deproj'+str(depIndex)+'\t\t',round(100.-ACT_eff[depIndex],2),'\t',round(ACT_mnu[tauIndex,depIndex],2),'\t',round(ACT_sn[tauIndex,depIndex],2)

for dep in ['0','1','3']:
    SO_eff = np.loadtxt('output/Apr17_mv_time_sens_deproj'+dep+'_iterOn_delensingEff.csv')
    SO_mnu = np.loadtxt('output/Apr17_deproj'+dep+'_tau_0.01_mnu.csv')
    SO_sn = np.loadtxt('output/Apr17_deproj'+dep+'_tau_0.01_sn.csv')

    print 'SO Baseline deproj'+dep+'\t',round(100.-SO_eff[timeIndex,sensIndex],2),'\t',round(SO_mnu[fskyIndex,sensIndex],2),'\t',round(SO_sn[fskyIndex,sensIndex],2)

print '\n-------LATEX VERSION-------'

print 'AdvACT deproj'+str(depIndex)+' &',round(100.-ACT_eff[depIndex],2),'&',round(ACT_mnu[tauIndex,depIndex],2),'&',round(ACT_sn[tauIndex,depIndex],2),'\\\\'

for dep in ['0','1','3']:
    SO_eff = np.loadtxt('output/Apr17_mv_time_sens_deproj'+dep+'_iterOn_delensingEff.csv')
    SO_mnu = np.loadtxt('output/Apr17_deproj'+dep+'_tau_0.01_mnu.csv')
    SO_sn = np.loadtxt('output/Apr17_deproj'+dep+'_tau_0.01_sn.csv')
    
    print 'SO Baseline deproj'+dep+'&',round(100.-SO_eff[timeIndex,sensIndex],2),'&',round(SO_mnu[fskyIndex,sensIndex],2),'&',round(SO_sn[fskyIndex,sensIndex],2),'\\\\'
