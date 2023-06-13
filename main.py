# code the Riemann hypothesis using the Riemann-Siegel formula and then plot the riemann zeta function using the Riemann-Siegel formula and
# the Euler-Maclaurin formula plot the time taken to calculate the Riemann-Siegel formula and the Euler-Maclaurin formula

import time

import matplotlib.pyplot as plt
import numpy as np


# Riemann-Siegel formula
def Riemann_Siegel(x):
    # x is the input value
    # returns the value of the Riemann-Siegel function at x
    if x < 0:
        return 0
    else:
        return np.sqrt(x / (2 * np.pi)) * np.sin(x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4)


# Euler-Maclaurin formula
def Euler_Maclaurin(x):
    # x is the input value
    # returns the value of the Euler-Maclaurin function at x
    if x < 0:
        return 0
    else:
        return np.sqrt(x / (2 * np.pi)) * np.sin(x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) + np.cos(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (8 * np.sqrt(x * np.pi)) - np.sin(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (48 * x * np.sqrt(x * np.pi)) - np.cos(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (384 * x ** 2 * np.sqrt(x * np.pi)) + np.sin(
            x / 2 + np.pi * np.sqrt(x) / 2 + np.pi / 4) / (9216 * x ** 3 * np.sqrt(x * np.pi))


# Riemann zeta function
def Riemann_zeta(x):
    # x is the input value
    # returns the value of the Riemann zeta function at x
    if x == 1:
        return np.inf
    else:
        return np.sum(1 / (np.arange(1, 10000) ** x))


# plot the Riemann zeta function using the Riemann-Siegel formula and the Euler-Maclaurin formula
x = np.linspace(0, 100, 1000)
y1 = np.zeros(1000)
y2 = np.zeros(1000)
for i in range(1000):
    y1[i] = Riemann_Siegel(x[i])
    y2[i] = Euler_Maclaurin(x[i])

plt.plot(x, y1, label='Riemann-Siegel formula')
plt.plot(x, y2, label='Euler-Maclaurin formula')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Riemann zeta function')
plt.legend()
plt.show()


# plot the time taken to calculate the Riemann-Siegel formula and the Euler-Maclaurin formula
x = np.linspace(0, 100, 1000)
y1 = np.zeros(1000)
y2 = np.zeros(1000)
for i in range(1000):
    start = time.time()
    Riemann_Siegel(x[i])
    end = time.time()
    y1[i] = end - start
    start = time.time()
    Euler_Maclaurin(x[i])
    end = time.time()
    y2[i] = end - start

plt.plot(x, y1, label='Riemann-Siegel formula')
plt.plot(x, y2, label='Euler-Maclaurin formula')
plt.xlabel('x')
plt.ylabel('time taken')
plt.title('time taken to calculate the Riemann-Siegel formula and the Euler-Maclaurin formula')
plt.legend()
plt.show()

