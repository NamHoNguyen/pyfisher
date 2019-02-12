from __future__ import print_function
from orphics import maps,io,cosmology,lensing
from enlib import enmap
import numpy as np
import os,sys
import cmblens
import cPickle as pickle
from pyfisher import lensInterface
from ConfigParser import SafeConfigParser

lmax = 7000
ells = np.arange(0,lmax,1)

fwhm = 1.3
kbeam = maps.gauss_beam(ells,fwhm)

ellmin_t = 300
ellmax_t = 3000
ellmin_e = ellmin_b = 100
ellmax_e = ellmax_b = 5000

ellmin_k = 20
ellmax_k = 5000

bin_edges = np.linspace(ellmin_k,ellmax_k,100)

noises = [10.]
ests = ['TT', 'EE','EB']

# set up pyfisher
expName = 'ACT_noatm'
Config = SafeConfigParser()
Config.optionxform=str
Config.read('./input/params.ini')

orphics_nls  = cmblens.util.create_dict(ests, noises)
pyfisher_nls = cmblens.util.create_dict(ests, noises) 
for noise in noises:
    ntt = (noise*np.pi/180./60.)**2. / kbeam**2.
    nee = 2.*ntt
    nbb = 2.*ntt
    
    ls,nlkks,theory,qest  = lensing.lensing_noise(ells,ntt,nee,nbb,
                      ellmin_t,ellmin_e,ellmin_b,
                      ellmax_t,ellmax_e,ellmax_b,
                      bin_edges,
                      ellmin_k = ellmin_k,
                      ellmax_k = ellmax_k,
                      camb_theory_file_root='/global/homes/d/dwhan89/cori/workspace/cmblens/inputParams/cosmo2017_10K_acc3',
                      estimators = ests,
                      delens = False,
                      theory=None,
                      dimensionless=False,
                      unlensed_equals_lensed=True,
                      grad_cut=None,
                      y_ells=None,y_ntt=None,y_nee=None,y_nbb=None,
                      y_ellmin_t=None,y_ellmin_e=None,y_ellmin_b=None,
                      y_ellmax_t=None,y_ellmax_e=None,y_ellmax_b=None,
                      lxcut_t=None,lycut_t=None,y_lxcut_t=None,y_lycut_t=None,
                      lxcut_e=None,lycut_e=None,y_lxcut_e=None,y_lycut_e=None,
                      lxcut_b=None,lycut_b=None,y_lxcut_b=None,y_lycut_b=None,
                      width_deg=10.,px_res_arcmin=1.)

    for est in ests:
        orphics_nls[est][noise] = nlkks[est]
        orphics_nls[est]['l']   = ls

    for est in ests:
        lensName = 'lens%s' % est
        ls, nl, _, _, _, _ = lensInterface.lensNoise(Config, expName, lensName, noiseTOverride=noise,\
                lkneeTOverride=None,lkneePOverride=None,alphaTOverride=None,alphaPOverride=None, deg=10., px=1.)
        pyfisher_nls[est][noise] = nl
        pyfisher_nls[est]['l']    = ls


pl = cmblens.visualize.plotter(yscale='log')
pl.add_data(ells,theory.gCl('kk',ells),color='k',lw=3)
for i,est in enumerate(ests):
    pl.add_data(orphics_nls[est]['l'], orphics_nls[est][10.],ls="-",color="C%d"%i,label=est)
    pl.add_data(pyfisher_nls[est]['l'], pyfisher_nls[est][10.],ls="--",color="C%d"%i)
pl.show_legends()
pl.set_xlim([0,2000])
pl.set_ylim([1e-8,1e-5])
pl.save("/global/homes/d/dwhan89/shared/outbox/cori/nltest.png")
