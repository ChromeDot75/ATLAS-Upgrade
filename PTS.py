import uproot 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import plotly.express as px

fh = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_2.root")
fh2 = uproot.open(r"N:\CERN\W5_Run_697\data\strun697_2.root")


h_scan = fh["h_scan0"]
h_scan2 = fh2["h_scan0"]

data_transposed = h_scan.values().T
data_transposed2 = h_scan2.values().T



fig = px.imshow(data_transposed, aspect='auto', labels=dict(x="Channel number", y="Counts"),
                title="Strobe Delay")

fig2 = px.imshow(data_transposed2, aspect='auto', labels=dict(x="Channel number", y="Counts"),
                title="Strobe Delay")

fig.update_layout(coloraxis_colorbar=dict(title="Counts"))
fig2.update_layout(coloraxis_colorbar=dict(title="Counts"))