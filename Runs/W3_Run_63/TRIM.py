import uproot 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


fh = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_2.root")

h_scan = fh["h_scan0"]

data_transposed = h_scan.values().T

fig, ax = plt.subplots() 


im = ax.imshow(data_transposed, aspect = 'auto')
colorbar = plt.colorbar(im, ax=ax)
#colorbar.set_label('Intensity')
plt.xlabel("Channel number")  
plt.ylabel("TRIMDAC [Counts]")  
plt.title("Pedestal Trim Test")
plt.show()  