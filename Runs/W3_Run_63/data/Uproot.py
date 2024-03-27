import uproot 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

print("Hello")
fh = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_3.root")

hist = fh['h_scan0;1']

values = hist.values()

plt.plot(values[1,:], '.')
plt.show()



def error_function(x, a, b, c): 
    return a * np.exp(-(x - b)**2 / (2 * c**2))

"""
print(vals[1000][0])
 
print(fh.keys())

print(dir(fh._keys))

print(fh.keys(recursive=False))

print(fh['h_scan0'])

projection_y = hist.ProjectionY()

print(projection_x, projection_y)

print(hist)

print(hist.values())

vals = hist.values()

print(vals[0,:])

print(len(vals)) 

"""