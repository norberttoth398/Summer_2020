Python scripts for use for NMF/PCA for cluster.


Script file structure within folder: (files such as README or binder build files are not shown)

├── PCA_scree_plot.py - script to create/plot PCA scree plots using Hyperspy.
├── cluster_size_comp_plag.py - script to calculate crystal size-composition data, specifically for Plag in this case but it may be eaily changed.
├── decompose.py - script to apply NMF to data.
└── mask_decompose.py - script to apply NMF to data after masking, allows NMF to be done only specific phases at a time.

