import vreg
import vreg.plot as plt
#
# Get the data:
#
kidneys = vreg.fetch('kidneys')
T1 = vreg.fetch('T1')
#
# Plot as overlays:
#
plt.overlay_2d(T1, kidneys)
