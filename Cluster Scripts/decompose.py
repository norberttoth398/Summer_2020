#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:53:48 2020

@author: norbert
"""
import matplotlib
import glob
from multiprocessing import Pool

#for headless mode:
matplotlib.rcParams["backend"] = "Agg"

import hyperspy.api as hs
hs.preferences.GUIs.warn_if_guis_are_missing = False
hs.preferences.save()


def decomp(mask_file):
	data = hs.load(mask_file)

	eds = data[2].copy()
	eds.change_dtype('float')

	eds.decomposition(True, algorithm = 'nmf', output_dimension = 6)

	eds.save("decomp/" + mask_file.split('.')[0] + "_decomp.hspy")
        #eds.learning_results.save("learn_result/" + mask_file.split('.')[0] + "_decomp.npz")


mask_files = ["insert names here"]

for item in mask_files:
	decomp(item)

#this can potentially be improved to multiprocessing functionality
#
#pool = Pool(processes =4)
#pool.map(decomp, mask_files)

