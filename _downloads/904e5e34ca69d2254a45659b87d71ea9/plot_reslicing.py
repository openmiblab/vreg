"""
====================================
Coronal, sagittal, axial and oblique
====================================

This examples illustrates how vreg can be used to slice 3D volumes in 
different ways.
"""

#%%
# Setup
# -----
import numpy as np
import vreg
import vreg.plot as plt

#%%
# Get data
# --------
# The starting point of this example is a 3D coronal volume of the abdomen. 
# For visual reference we'll also load a 3D coronal mask of the kidneys.

# 3D coronal volume of the abdomen
cor = vreg.fetch('Dixon_out_phase')

# 3D coronal mask of the kidneys
mask = vreg.fetch('kidneys')

# Show the data
plt.overlay_2d(cor, mask, alpha=1.0, width=6)

#%%
# Coronal -> Axial
# ----------------
# We reslice the coronal volume in the axial plane using an isotropic 1mm 
# voxel size. Since 1mm is the default spacing, we do not have to specify it 
# explicitly.

# Reslice isotropically in the axial plane
axial = cor.reslice(orient='axial')

# Show the result
plt.overlay_2d(axial, mask, alpha=1.0, width=6)

#%%
# Axial -> Sagittal
# -----------------
# Since vreg keeps track of the position in space, we can keep reslicing the 
# result. Let's reslice the axial volume sagitally:

# Reslice isotropically in the sagittal plane
sagit = axial.reslice(orient='sagittal')

# Show the result
plt.overlay_2d(sagit, mask, alpha=1.0, width=6)

#%%
# Sagittal -> Coronal
# -------------------
# As a consistency check, we can reslice the sagittal volume coronally again 
# and check against the original  

# Sagittal to coronal
cor = sagit.reslice(orient='coronal')

# Compare result to the original
plt.overlay_2d(cor, mask, alpha=1.0, width=6)

#%%
# As expected, this looks visually the same as the original coronal image. 
# The number of slices is increased because this now has a 1mm isotropic voxel 
# size, whereas the original had 1.5mm slice thickness. 

#%%
# Oblique
# -------
# The oblique orientation refers to any that is not in one of the standard 
# plances (coronal, sagittal or axial). A volume can be reslice to any oblique 
# orientation by specifying a rotation vector.
#
# As an example, let's reslice the coronal volume obliquely along the principle 
# axis of the kidneys. The sagittal images shows that the kidneys make an 
# angle of approximately 30 degrees with the vertical (z-axis). 
# 
# If we reslice the coronal volume using a rotation of -30 degrees around 
# the x-axis, we get a coronal-oblique view through the kidneys:

obl = cor.reslice(rotation=[-np.radians(30), 0, 0])

# Show the oblique reslice:
plt.overlay_2d(obl, mask, alpha=1.0, width=6)

#%%
# Oblique in the sagittal plane
# -----------------------------
# The oblique image above cuts along the natural axis of the kidneys. We 
# can verify this visually by looking at this oblique section in the sagittal 
# plane:

obl = cor.reslice(orient='sagittal', rotation=[-np.radians(30), 0, 0])

# Show the sagittal-oblique view
plt.overlay_2d(obl, mask, alpha=1.0, width=6)


