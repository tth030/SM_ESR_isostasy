#!/usr/bin/env python

from . import geodyn1d
from .geodyn1d.tools import *
from .book_deltarho import *
from copy import deepcopy

def compute_rhoref_along_geotherm(perplex,
                                  lithos=None,
                                  temperature_shift=0,
                                  use_readrho=False):
    ''' 
        Compute reference density, i.e. at surface conditions (use_readrho=False), with its standard deviation.
        along a given geotherm based
    '''
        
    Tref  = 273
    Pref  = 0
    rho   = deepcopy(perplex.rho)
    T     = deepcopy(perplex.T)
    P     = deepcopy(perplex.P)
    alpha = deepcopy(perplex.alpha)
    beta  = deepcopy(perplex.beta)
    melt  = deepcopy(perplex.melt)
    
    factor1 = 1 + np.multiply(beta,P-Pref)
    factor2 = 1 - np.multiply(alpha,T-Tref)
    factor  = np.multiply(factor1,factor2)
    rhoref = np.divide(rho,factor)
    if (use_readrho):
        rhoref = rho
    
    if ( lithos is None ):
        print('Lithosphere lith125 used as default to compute rhoref')
        lithos = geodyn1d.lithosphere('lith125')

    if ( isinstance(lithos, str) ):
        lithos = geodyn1d.lithosphere(lithos)
    pmax = np.max(perplex.P)
    tmax = np.max(perplex.T)
    T = np.linspace(np.min(perplex.T),
                    tmax,
                    perplex.nt)
    P = np.linspace(np.min(perplex.P),
                    pmax,
                    perplex.np)
    f      = RegularGridInterpolator((np.array(P)/pmax, np.array(T)/tmax), rhoref.reshape(perplex.np,perplex.nt))
    f_melt = RegularGridInterpolator((np.array(P)/pmax, np.array(T)/tmax), perplex.melt.reshape(perplex.np,perplex.nt))
    
    # we check for geotherm and pressure profile
    if ( not lithos.geotherm):
        lithos.get_steady_state_geotherm(printOut=False)
    if ( not lithos.P_rho_DepthProfile):
        lithos.get_pressure_density_profile(printOut=False)
    
    sort_rhoref = []
    sort_melt     = []
    for i in range(0,len(lithos.geotherm.Z)):
        pressure = lithos.P_rho_DepthProfile.P[i]
        temp     = lithos.geotherm.T[i] + temperature_shift
        melt_read = f_melt([pressure/pmax,temp/tmax])
        if (melt_read>0):
            sort_rhoref.append(f([pressure/pmax,temp/tmax]))
            sort_melt.append(melt_read)
    sort_melt = [i * 100 for i in sort_melt]
        
    return sort_melt, sort_rhoref


def update_mantle_density(name,book,perplex_name='slm_sp2008',rhoc0=2860):
    '''
       Update mantle parameters to use perplex grids to compute density
    '''
    newbook    = book
    allmantles = { 'matLM1', 'matLM2', 'matLM3', 'matSLM' }

    if perplex_name:
        newbook = update_use_tidv(allmantles,newbook,7)
        newbook = update_perplex_name(allmantles,newbook,perplex_name)
        newbook = update_deltarho(allmantles,newbook,name,perplex_name,use_perplex=True,rhoc0=rhoc0) # should be run after update_perplex_name if use_perplex is True
    else:
        newbook = update_use_tidv(allmantles,newbook,1)
        newbook = update_deltarho(allmantles,newbook,name,perplex_name,use_perplex=False,rhoc0=rhoc0)
    return newbook

def update_use_tidv(allmaterials,book,num):
    '''
       1: use thermal expansion only
       7: use perplex table to compute the density
    '''
    newbook = book
    for material in allmaterials:
        newbook[material]['use_tidv'] = num
    return newbook

def update_perplex_name(allmaterials,book,perplex_name):
    '''
      name: perplex grid name that refers to the composition
    '''
    newbook = book
    for material in allmaterials:
        if material == 'matSLM':
            newbook[material]['perplex_name'] = 'slm_sp2008' # default reference fertile sub-lithospheric mantle composition
        else:
            newbook[material]['perplex_name'] = perplex_name
    return newbook

def update_deltarho(allmaterials,book,name,perplex_name='slm_sp2008',use_perplex=False,rhoc0=2860):
    '''
      name: lithosphere name
    '''
    newbook = book
    for material in allmaterials:
        if material == 'matSLM':
            deltarho = 0
        else:
            deltarho = find_drho(perplex_name,name,use_perplex,rhoc0)
        newbook[material]['deltarho'] = deltarho
    return newbook

def find_drho(perplex_name='slm_sp2008',name='lith125',use_perplex=False,rhoc0=2860):
    '''
       type = 'perplex' or 'onlytempdep'
    '''
    book=book_deltarho # database valuable for rhoc0 == 2860 kg/m3 
    if rhoc0==2860:
        if use_perplex:
            if name not in book['perplex']:
                print("ERROR: Lithosphere name is unknown ("+name+")")
                quit()
            if perplex_name in book['perplex'][name]:
                deltarho = book['perplex'][name][perplex_name]
            else:
                print("WARNING: reference deltarho for this composition ("+perplex_name+") and this lithosphere ("+name+") is unknown. We use deltarho = 0")
                deltarho = 0
        else:
            if name not in book['onlytempdep']:
                print("ERROR: Lithosphere name is unknown ("+name+")")
                quit()
            deltarho = book['onlytempdep'][name]
    else:
        print("ERROR: Not implemented yet with different crustal density than 2860 kg/m3")
        quit()
    return deltarho
