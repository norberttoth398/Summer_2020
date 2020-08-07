#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:41:49 2020

@author: norbert
"""


import matplotlib.pyplot as plt
import cv2
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


def QEMSCANMask_2_CSD(name, scale, min_size, max_size, n_bins, correct_for_edge = False, edge_width = 0):
    """
    Function taking a .png phase mask in RGB colourspace from QEMSCAN to create approximate CSD,
    as described in Neave et. al. (2017), using Area^{0.5} as measure of length without
    stereological correction.
    
    Parameters
    ----------
    name : string
        File name to be loaded in for analysis.
    scale : int
        Spatial resolution of each pixel in image.
    Correct_for_edge: bool
        Signal to show whether any areas from edges is to be removed prior to processing
            - found to be required for QEMSCAN at times.
    edge_width: int
        Width of any edge area to be removed prior to processing.
    min_size: int
        Minimum size (area^{0.5}) used for binning/plotting process.
    max_size: int
        Maximum size (area^{0.5}) used for binning/plotting process.
    n_bins: int
        Number of bins used.        

    Returns
    -------
    fig : Matplotlib figure object 
        Figure object of plot created.
    ax : Matplotlib axis object
        Axis object of plot created.

    """
    
    #load image and process it, resulting in binary phase mask
    img = cv2.imread(name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, phase_mask = cv2.threshold(gray, 2, 255, cv2.THRESH_BINARY)
    phase_mask[phase_mask == 255] = 1

    #sometimes a strip of 1's exist for QEMSCAN images around the edges causing
    #issues later - if present they can be simply removed however.
    if correct_for_edge == True:
        for i in range(edge_width):
            for j in range(len(phase_mask)):
                phase_mask[j][i] = 0
            for q in range(len(phase_mask[i])):
                phase_mask[i][q] = 0
    
        for i in range(edge_width):
            for j in range(len(phase_mask)):
                phase_mask[j][len(phase_mask[0]) - i-1] = 0
            for q in range(len(phase_mask[i])):
                phase_mask[len(phase_mask) - i-1][q] = 0
    else:
        pass
    
    #create a binary mask of filled crystals (holes removed) so approximation with area is more realistic
    bare_mask = phase_mask.copy()
    contours, _ = cv2.findContours(bare_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bare_pic = np.zeros((len(bare_mask),len(bare_mask[1])))
    mask_filled = cv2.drawContours(bare_pic, contours, -1, 1, thickness = cv2.FILLED)
    
    #label regions to be identified as different crystals based on connectivity
    label_mask = morphology.label(mask_filled, connectivity = 1)
    props = measure.regionprops(label_mask)
    
    
    properties = []
    #remove any crystals which are too small to measure with the present soatial resolution
    for item in props:
        if item.major_axis_length == 0:
            pass
        elif item.minor_axis_length == 0:
            pass
        else:
            properties.append(item)
            
    size = [sqrt(item.area)*scale for item in properties]
    
    section_area = scale**2 * len(phase_mask)*len(phase_mask[0])

    #generate approx CSD plot from data gathered from image
    fig,ax = gen_csd_plot(size, min_size, max_size, n_bins, section_area)

    return fig, ax
