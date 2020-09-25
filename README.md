[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tothnorbi98/2020_summer/d0b136c2d05a9ba2cba0341c183b24195bcd29eb)

# EDS Analysis - Summer 2020
Machine Learning and Image segmentation for EDS crystal shape and size analysis in Cambridge ES. <br/>


To launch binder environment for "ExampleTexturalProcessing.ipynb" notebook, use: https://mybinder.org/v2/gh/tothnorbi98/2020_summer/d0b136c2d05a9ba2cba0341c183b24195bcd29eb. <br/>

<pre>
Script file structure within repository: (files such as README or binder build files are not shown) 

├── Cluster Scripts - folder containing scripts written to run/execute tasks requiring the cluster. 
|   ├── PCA_scree_plot.py - script to create/plot PCA scree plots using Hyperspy. 
|   ├── cluster_size_comp_plag.py - script to calculate crystal size-composition data, specifically for Plag in this case but it may be eaily changed. 
|   ├── decompose.py - script to apply NMF to data.
|   └── mask_decompose.py - script to apply NMF to data after masking, allows NMF to be done only specific phases at a time.
|
├── Elliptical Fourier - folder containing EFA/EFD notebook
|   └── EFD_withPCA.ipynb - jupyter notebook showing an approach (nowhere near perfect) to use EFD's combined with PCA to probe crystal shapes.
|
├──Textural Processing
|   ├── Approx_CSD_generators.py - collection of functions used to plot approximate CSD plots (as in Neave et. al. (2017)); may be used in binder environment
|   ├── ExampleTexturalProcessing.ipynb - binder executable notebook showing how textural data may be processed using this method (use launch tag or link)
|   ├── QEMSCAN_PhaseMask_2_CSD.py - script with functions able to turn a QEMSCAN phase mask into approximate CSD.
|   └── Useful_funcs.py - collection of useful Python functions, may be used in binder environment.
</pre>

