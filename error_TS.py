import uproot
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import erfc
import plotly.graph_objects as go

# Open ROOT file and get histogram
fh = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_4.root")
hist = fh['h_scan0;1']
values = hist.values()[1]
x_values = np.linspace(0, 80, len(values))

# Define the complementary error function (erfc) as the fitting function
def erfc_fit(x, A, mu, sigma, offset):
    return A * erfc((x - mu) / (sigma * np.sqrt(2))) + offset

# Initial guess for the parameters
initial_guess = [1.0, np.mean(x_values), np.std(x_values), 0.0]

# Fit the data to the erfc function
params, covariance = curve_fit(erfc_fit, x_values, values, p0=initial_guess)

# Generate y values using the fitted parameters
y_fit = erfc_fit(x_values, *params)

equation = f"y = {params[0]:.4f} * erfc((x - {params[1]:.4f}) / ({params[2]:.4f} * sqrt(2))) + {params[3]:.4f}"
print("Fitted Equation:", equation)

x_point = 21.96
y_point = 511.45

# Scatter plot for mean point
scatter_trace = go.Scatter(
    x=[x_point],
    y=[y_point],
    mode='markers',
    marker=dict(color='green', symbol='circle', size=12),  # Increased marker size
    name='mean'
)

# Original data points
data_trace = go.Scatter(
    x=x_values,
    y=values,
    mode='lines+markers',
    name='Data Points',
    marker=dict(size=8)  # Adjust marker size
)

# Fitted erfc function
fit_trace = go.Scatter(
    x=x_values,
    y=y_fit,
    mode='lines',
    name='Fitted erfc',
    line=dict(dash='dash')
)

# Layout
layout = go.Layout(
    title='Threshold scan fitted with a complementary error function',
    xaxis=dict(title='Threshold [mV]'),
    yaxis=dict(title='n [Events]'),
)

# Create figure and add traces
fig = go.Figure(data=[scatter_trace, data_trace, fit_trace], layout=layout)

fig.show()
