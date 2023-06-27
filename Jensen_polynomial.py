# code jensen polynomial and plot the jensen polynomial

import matplotlib.pyplot as plt
import numpy as np


# Jensen polynomial
def Jensen_polynomial(x):
    # x is the input value
    # returns the value of the Jensen polynomial at x
    if x == 1:
        return np.inf
    else:
        return np.sum(1 / (np.arange(1, 10000) ** x))


# plot the Jensen polynomial
x = np.linspace(0, 10, 1000)
y = np.zeros(1000)
for i in range(1000):
    y[i] = Jensen_polynomial(x[i])

plt.plot(x, y, label='Jensen polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Jensen polynomial')
plt.legend()
plt.show()
