#IV 
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

class JsonData:

    def __init__(self, json_FP):
        with open(json_FP) as file:
            data = json.load(file)
            self.results = data.get('results', {}) #starts search when sees this keyword and braces
    

    def get_current(self):
        return self.results.get('CURRENT', [])    
    
    def get_voltage(self):
        return self.results.get('VOLTAGE', [])

"""
def plot_iv_graph(json_file_path, figure=None):
    json_data = JsonData(json_file_path)
    currents = json_data.get_current()
    voltages = json_data.get_voltage()
"""
    
json_data = JsonData("N:\\CERN\\W3_Run_63\\results\\SN20USBHX2001092_UNKNOWN_20231009_63_18_MODULE_IV_AMAC.json")
json_data2 = JsonData("N:\\CERN\\W5_Run_697\\results\\SN20USBHX2001216_UNKNOWN_20231026_697_1_MODULE_IV_AMAC.json")
currents, currents2 = json_data.get_current(), json_data2.get_current()     #applies function to json_data & give them to 2 arrays of current & voltage
voltages, voltages2 = json_data.get_voltage(), json_data2.get_voltage() 



fig = go.Figure()
fig2 = go.Figure()

fig.add_trace(go.Scatter(x=voltages, y=currents, mode='lines', marker=dict(size=8)))#
fig2.add_trace(go.Scatter(x=voltages, y=currents, mode='lines', marker=dict(size=8)))


# Set layout options
fig.update_layout(
    title="IV SCAN",
    xaxis=dict(title="Bias Voltage [V]"),
    yaxis=dict(title="Current [μA]"),
    font=dict(family="FreeSerif", size=22)
)

fig2.update_layout(
    title="IV SCAN",
    xaxis=dict(title="Bias Voltage [V]"),
    yaxis=dict(title="Current [μA]"),
    font=dict(family="FreeSerif", size=22)
)




