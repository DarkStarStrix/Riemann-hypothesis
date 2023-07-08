# code the L-Functions and plot the L-Functions dirichlet series

import matplotlib.pyplot as plt
import numpy as np


# L-Functions dirichlet series
def L_Functions(x):
    # x is the input value
    # returns the value of the L-Functions dirichlet series at x
    if x == 1:
        return np.inf
    else:
        return np.sum(1 / (np.arange(1, 10000) ** x))


# plot the L-Functions dirichlet series
x = np.linspace(0, 10, 1000)
y = np.zeros(1000)
for i in range(1000):
    y[i] = L_Functions(x[i])

plt.plot(x, y, label='L-Functions dirichlet series')
plt.xlabel('x')
plt.ylabel('y')
plt.title('L-Functions dirichlet series')
plt.legend()
plt.show()
