import uproot 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from scipy.special import erf
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px




def TS_func(module, stream):
    fh = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_4.root")
    fh2 = uproot.open(r"N:\CERN\W5_Run_697\data\strun697_4.root")
    hist = fh[f'h_scan{module};{stream}']
    hist2 = fh2[f'h_scan{module};{stream}']

    data_transposed = hist.values().T
    data_transposed2 = hist2.values().T

    fig, ax = plt.subplots() 
    fig2, ax = plt.subplots() 

    df = pd.DataFrame(data_transposed)
    df2 = pd.DataFrame(data_transposed2)


    fig = px.imshow(df, aspect='auto', labels=dict(x="Channel number", y="Counts"),
                    title="Strobe Delay")

    fig.update_layout(coloraxis_colorbar=dict(title="Counts"))

    fig2 = px.imshow(df2, aspect='auto', labels=dict(x="Channel number", y="Counts"),
                    title="Strobe Delay")

    fig2.update_layout(coloraxis_colorbar=dict(title="Counts"))
    return fig2







#plt.show()

#
"""
print(f"Fitted Parameters: a = {params[0]}, b = {params[1]}, c = {params[2]}")

ax.imshow() - Put into 

counts, synchoseconds, to find units for time in strobe delay. 

S-curve VT50 explains define it. midpoint, mean of gaussian. 

VT50 mean and average of the chips after 10 traces. 

plt.plot(values[1,:], '.')
plt.show()

"""