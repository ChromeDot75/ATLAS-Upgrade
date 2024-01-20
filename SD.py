import uproot 
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import plotly.tools as tls

fh = uproot.open(r".\W3_Run_63\data\strun63_3.root")
fh2 = uproot.open(r".\W5_Run_697\data\strun697_3.root")

h_scan = fh["h_scan0"]
h_scan2 = fh2["h_scan0"]

data_transposed = h_scan.values().T
data_transposed2 = h_scan2.values().T

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