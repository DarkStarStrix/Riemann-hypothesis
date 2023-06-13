# using matplotlib code rienmann geometry and visualizing the riemann zeta function using the Riemann-Siegel formula and the Euler-Maclaurin formula

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


# plot rienmann manifolds using the Riemann-Siegel formula and the Euler-Maclaurin formula using 3d plots
x = np.linspace(0, 100, 1000)
y = np.linspace(0, 100, 1000)
X, Y = np.meshgrid(x, y)
Z1 = np.zeros((1000, 1000))
Z2 = np.zeros((1000, 1000))
for i in range(1000):
    for j in range(1000):
        Z1[i][j] = Riemann_Siegel(X[i][j])
        Z2[i][j] = Euler_Maclaurin(X[i][j])

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_title('Riemann-Siegel formula')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(60, 35)
plt.show()

# calculate the time taken to calculate the Riemann-Siegel formula and the Euler-Maclaurin formula and plot

# Riemann-Siegel formula
start = time.time()
Riemann_Siegel(100)
end = time.time()
print("Time taken to calculate the Riemann-Siegel formula: ", end - start)

# Euler-Maclaurin formula
start = time.time()
Euler_Maclaurin(100)
end = time.time()
print("Time taken to calculate the Euler-Maclaurin formula: ", end - start)

# plot the time complexity of the Riemann-Siegel formula and the Euler-Maclaurin formula using asymptotic notation
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
plt.title('Time complexity of the Riemann-Siegel formula and the Euler-Maclaurin formula')
plt.legend()
plt.show()


