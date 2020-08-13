[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tothnorbi98/Summer_2020/87e43b2860fb4b01cea4cba2324befe3e2613de0)

# Summer_2020
Machine Learning and Image segmentation for EDS crystal shape and size analysis in Cambridge ES. <br/>


To launch binder environment for "ExampleTexturalProcessing.ipynb" notebook, use: https://mybinder.org/v2/gh/tothnorbi98/Summer_2020/87e43b2860fb4b01cea4cba2324befe3e2613de0. <br/>

<pre>
Script file structure within repository: (files such as README or binder build files are not shown) <br/>
<br/>
├── Cluster Scripts - folder containing scripts written to run/execute tasks requiring the cluster. <br/>
|   ├── PCA_scree_plot.py - script to create/plot PCA scree plots using Hyperspy. <br/>
|   ├── cluster_size_comp_plag.py - script to calculate crystal size-composition data, specifically for Plag in this case but it may be eaily changed. <br/>
|   ├── decompose.py - script to apply NMF to data.<br/>
|   └── mask_decompose.py - script to apply NMF to data after masking, allows NMF to be done only specific phases at a time.<br/>
|<br/>
├── Elliptical Fourier - folder containing EFA/EFD notebook<br/>
|   └── EFD_withPCA.ipynb - jupyter notebook showing an approach (nowhere near perfect) to use EFD's combined with PCA to probe crystal shapes.<br/>
|<br/>
├── Approx_CSD_generators.py - collection of functions used to plot approximate CSD plots (as in Neave et. al. (2017)); may be used in binder environment<br/>
├── ExampleTexturalProcessing.ipynb - binder executable notebook showing how textural data may be processed using this method (use launch tag or link)<br/>
├── QEMSCAN_PhaseMask_2_CSD.py - script with functions able to turn a QEMSCAN phase mask into approximate CSD.<br/>
└── Useful_funcs.py - collection of useful Python functions, may be used in binder environment.<br/>
</pre>

