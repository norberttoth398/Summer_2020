#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 13:36:50 2020

@author: norbert
"""

import matplotlib
matplotlib.rcParams["backend"] = "Agg"
import hyperspy.api as hs
import numpy as np
import matplotlib.pyplot as plt
import glob

def save_scree_hspy(file):
	"""
	Creates and saves PCA scree plot using Hyperspy.
	"""
	a = hs.load(file)
	s = a[2]
	s.change_dtype('float32')
	name = file.split('.')[0]

	s.decomposition(True, algorithm='svd', output_dimension=15)

	scree = s.plot_explained_variance_ratio()
	scree.figure.savefig(name + "_scree.png", dpi = 300)


files = ["insert file names"]
for item in files:
	save_scree_hspy(item)
