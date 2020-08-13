#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:21:48 2020

@author: norbert
"""

import matplotlib

#for headless mode:
matplotlib.rcParams["backend"] = "Agg"

import hyperspy.api as hs
import numpy as np
from skimage import measure

import glob
from multiprocessing import Pool


names =["wat_plag/watershed_JM1_OL7.npz", "wat_plag/watershed_JM1_OL24.npz"]

def split_at(string, char, n):
    """
    Splits string into two at the nth occurence of the character specified.
    
    Input
    ------------------------------------
    string - string to be split into two
    char - character to split at
    n - the occurrence of character at which splitting should occur.
    
    Returns
    -------------------------------------
    The two ends of the string split at the specified position.
    """
    words = string.split(char)
    return char.join(words[:n]), char.join(words[n:])

def extract_comp_size(mask_name, parent):
    """
    
    Parameters
    ----------
    mask_name : string
        name of .npz library containing mask
    parent : string
        name of .bcf parent file containing EDS data

    Returns
    -------
    None.

    """
    
    data = np.load(mask_name)

    eds_data = hs.load(parent)
    mask = data['plg'].copy()
    eds = eds_data[2]
    
    label = measure.label(mask, connectivity = 1)
    props = measure.regionprops(label)
    coords = [prop.coords for prop in props]
    sqrt_area = data['size']

    
    ca_si_ratio = []
    Ca_content = []
    
    for cryst in coords:
        
        Si = 0
        Ca = 0

        for i in range(len(cryst)):
            Ca += eds.inav[cryst[i][1]].inav[cryst[i][0]].get_lines_intensity(['Ca_Ka'])[0].data
            Si += eds.inav[cryst[i][1]].inav[cryst[i][0]].get_lines_intensity(['Si_Ka'])[0].data

        Ca = Ca / len(cryst)
        Si = Si / len(cryst)
        ratio = Ca/Si
        ca_si_ratio.append(ratio)
        Ca_content.append(Ca)
        
    
    np.savez("size_comp_data_" + mask_name.split('.')[0] + ".npz", size = sqrt_area, comp = ca_si_ratio, Ca = Ca_content)
    print("done")
    
    

    
#the below can be autmatically generated using functions, depending on how the files
#are named and stored.
names =["insert .npz file names"]
parent = ["insert names of corresponding .bcf files"]

for n in range(len(names)):
    extract_comp_size(names[n], parent[n])


#this can potentially be improved to multiprocessing functionality
#
#pool = Pool(processes =4)
#pool.map(extract_comp_size, names, parent, file_name)



