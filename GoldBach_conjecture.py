# code the GoldBach conjecture and plot the GoldBach conjecture

import matplotlib.pyplot as plt
import numpy as np


# GoldBach conjecture
def GoldBach_conjecture(x):
    # x is the input value
    # returns the value of the GoldBach conjecture at x
    if x == 1:
        return np.inf
    else:
        return np.sum(1 / (np.arange(1, 10000) ** x))


# plot the GoldBach conjecture in the interval [0, 10] with 1000 points
x = np.linspace(0, 10, 1000)
y = np.zeros(1000)
for i in range(1000):
    y[i] = GoldBach_conjecture(x[i])

plt.plot(x, y, label='GoldBach conjecture')
plt.xlabel('x')
plt.ylabel('y')
plt.title('GoldBach conjecture')
plt.legend()
plt.show()
