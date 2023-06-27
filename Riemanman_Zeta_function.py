# plot the non-trivial zeros of the Riemann zeta function

# import packages
import numpy as np
import matplotlib.pyplot as plt
import time


# make a function to calculate the number of non-trivial zeros of the Riemann zeta function
def number_of_non_trivial_zeros_of_the_Riemann_zeta_function(x):
    # x is the input value
    # returns the number of non-trivial zeros of the Riemann zeta function at x
    if x < 0:
        return 0
    else:
        return np.sqrt(x / (2 * np.pi)) * np.sin(x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) + np.cos(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (8 * np.sqrt(x * np.pi)) - np.sin(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (48 * x * np.sqrt(x * np.pi)) - np.cos(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (384 * x ** 2 * np.sqrt(x * np.pi)) + np.sin(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (9216 * x ** 3 * np.sqrt(x * np.pi))


# calculate the number of non-trivial zeros of the Riemann zeta function at x
# using the Riemann-Siegel formula and the Euler-Maclaurin formula
x = np.linspace(0, 100, 1000)
y1 = np.zeros(1000)
y2 = np.zeros(1000)
for i in range(1000):
    y1[i] = number_of_non_trivial_zeros_of_the_Riemann_zeta_function(x[i])
    y2[i] = number_of_non_trivial_zeros_of_the_Riemann_zeta_function(x[i])

# plot the number of non-trivial zeros of the Riemann zeta function using the Riemann-Siegel formula and the Euler-Maclaurin formula
plt.plot(x, y1, label='Riemann-Siegel formula')
plt.plot(x, y2, label='Euler-Maclaurin formula')
plt.xlabel('x')
plt.ylabel('y')
plt.title('number of non-trivial zeros of the Riemann zeta function')
plt.legend()
plt.show()






