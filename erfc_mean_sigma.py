#Median and sigma for erfc

import scipy.special
from scipy.optimize import root_scalar

# Given parameters
mu = 21.9579
sigma = -2.1605 * (2 ** 0.5)

# Define the equation to find the median
equation = lambda x: 0.5 - 0.5 * scipy.special.erfc((x - mu) / (sigma * (2 ** 0.5)))

# Use root_scalar to find the root of the equation (i.e., where equation(x) = 0)
result = root_scalar(equation, bracket=[mu - 10, mu + 10])

# The result object contains the median value
median_value = result.root

y_value = -511.1926 * scipy.special.erfc((median_value - mu) / (sigma * (2 ** 0.5))) + 1022.6386

print(y_value)
print(median_value)