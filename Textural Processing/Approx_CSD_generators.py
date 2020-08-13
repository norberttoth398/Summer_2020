#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:41:49 2020

@author: norbert
"""


import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt

from skimage import morphology, measure



def geo_factor(min_size, max_size, n_bins):
    """
    Calculate the geometric factor required to establish bins.
    
    Input
    --------------------------------------
    min_size - lower bound of binning process
    max_size - upper bound of binning
    n_bins - number of bins generated 
    
    Returns
    --------------------------------------
    factor - the geometric factor required for the binning process
    correction - log (base factor) of lower bound of the binning process
    """
    ratio = max_size/min_size
    factor = ratio**(1/n_bins)
    correction = np.log(min_size)/np.log(factor)
    return factor, correction
    
    
def gen_geo_bins(min_size, max_size, n_bins):
    """
    Generate geometric bins required.
    
    Input
    ----------------------------------
    min_size - lower bound of binning process
    max_size - upper bound of binning
    n_bins - number of bins generated   
    
    Returns
    -----------------------------------------------------
    bins - lower bound for each bin
    bw - bin widths
    x_grid - middle values for the bins to be used for plot
    """
    factor, correction = geo_factor(min_size, max_size, n_bins)
    
    bins = [factor**(i+correction) for i in range(n_bins)]
    bw = [(factor**(i+1 + correction) - factor**(i + correction)) for i in range(n_bins)]
    x_grid = [(factor**(i+1 + correction) + factor**(i + correction))/2 for i in range(n_bins)]
    
    return bins, bw, x_grid

def gen_csd_plot(size, min_size, max_size, n_bins, area):
    """
    Create approximate CSD plot (Neave et. al. 2017) using geometric binning.
    
    Inputs
    ----------------------------------------------
    size - array of crystal sizes
    min_size - lower bound of binning process
    max_size - upper bound of binning
    n_bins - number of bins generated 
    area - area of ROI considered
    
    Returns
    -----------------------------------------------
    fig - matplotlib figure object containing the CSD plot
    ax - matplotlib axis object for fig above
    """
    
    #run functions to generate bins and all required parameters
    factor, correction = geo_factor(min_size, max_size, n_bins)
    bins, bw, x_grid = gen_geo_bins(min_size, max_size, n_bins)
        
    n_cryst = np.zeros(n_bins)

    #apply binning to data
    for i in range(len(size)):
        if size[i] >= max_size:
            pass
        elif size[i] < min_size:
            pass
        else:
            index = int((np.log(size[i])/np.log(factor))-correction)
            n_cryst[index] += 1
    
    #generate y axis data
    n_cryst_div_bw = [(n_cryst[i]/bw[i])/area for i in range(n_bins)]
    ln_cryst_div_bw = np.log(n_cryst_div_bw)
    
    #create matplotlib plot that is then returned
    fig, ax = plt.subplots()
    
    ax.plot(x_grid, ln_cryst_div_bw, '.', markersize = 11)
    ax.set_xlabel(r"Area$^{0.5}$ ($\mu$m)")
    ax.set_ylabel("ln(N / bw)")
    
    fig.show()
    
    return fig, ax

