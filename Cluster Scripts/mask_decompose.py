#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:24:17 2020

@author: norbert
"""
import hyperspy.api as hs
import numpy as np
#import glob

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


def decompose(mask_file, parent, n_phases):
    """
    Perform NMF on EDS map after glass mask is applied by assigning an empty spectrum to each pixel
    equal to zero in the bianry mask.
    
    Parameters
    ----------
    mask_file : string
        name of .npz library containing mask
    parent : string
        name of parent .bcf file
    n_phases : int
        number of NMF outputs

    Returns
    -------
    None.

    """

    glass_data = np.load(mask_file)
    glass = glass_data['mask']
    
    bcf_data = hs.load(parent)
    eds = bcf_data[2].copy()
    
    dummy_spec = np.zeros(2048)
    
    for i in range(len(glass)):
        for j in range(len(glass[i])):
            if glass[i][j] == 0:
                eds.inav[j].inav[i].data = dummy_spec.copy()
            else:
                pass
            
    eds.change_dtype('float')
    
    eds.decomposition(True, algorithm = 'nmf', output_dimension =n_phases)
    eds.save(mask_file.split('.')[0] + "_decomp.hspy")

    #eds.learning_results.save(mask_file.split('.')[0] + "_decomp.npz")
    
 

#to execute
files = ["insert file names here"]
parent_files = ["insert file names here"]


for n in range(len(files)):

    decompose(files[n], parent_files[n], "number of phases to be decomposed to" )




















