import uproot 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from scipy.special import erf


fh = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_4.root")
fh2 = uproot.open(r"N:\CERN\W5_Run_697\data\strun697_4.root")
hist = fh['h_scan0;1']
hist2 = fh2['h_scan0;1']

values = hist.values()[1]
values2 = hist2.values()[1]
print(type(values))

#plt.plot(values, '.')

# Define the error function you want to fit
def error_function(x, a, b, c, d):
    return a * np.exp(-(x - b)**2 / (2 * c**2)) + d

# Create an array of x values corresponding to your data points
x_values = np.arange(len(values))
x_values2 = np.arange(len(values2))


# Fit the error function to the data
initial_guess = [1, np.argmax(values), 1, 0]  # Adjust the initial guess as needed
fit_params, _ = curve_fit(error_function, x_values, values, p0=initial_guess)
fit_params2, _ = curve_fit(error_function, x_values2, values2, p0=initial_guess)
# Generate y values for the fitted curve
fit_curve = error_function(x_values, *fit_params)
fit_curve2 = error_function(x_values2, *fit_params)

# Plot the data and the fitted curve
plt.plot(x_values, values, label='Data')
plt.plot(x_values, fit_curve, label='Fitted Error Function', linestyle='--')
plt.legend()
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Error Function Fit to Data')
plt.show()







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