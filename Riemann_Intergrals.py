# code riemann integral and riemann sum and plot the riemann sum

import time
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate


# Riemann integral
def Riemann_integral(f, a, b, n):
    # f is the function to be integrated
    # an is the lower bound of the integral
    # b is the upper bound of the integral
    # n is the number of subintervals
    # returns the value of the Riemann integral of f from a to b
    x = np.linspace(a, b, n + 1)
    y = f(x)
    dx = (b - a) / n
    return np.sum(y * dx)


# Riemann sum
def Riemann_sum(f, a, b, n):
    # f is the function to be integrated
    # an is the lower bound of the integral
    # b is the upper bound of the integral
    # n is the number of subintervals
    # returns the value of the Riemann sum of f from a to b
    x = np.linspace(a, b, n + 1)
    y = f(x)
    dx = (b - a) / n
    return np.sum(y * dx)


# calculate the Riemann sum in comparison to the Riemann integral and the scipy.integrate.quad function and plot the time taken to calculate the Riemann sum and the Riemann integral in 3d'
start_time = time.time()
x = np.linspace(0, 100, 1000)
y1 = np.zeros(1000)
y2 = np.zeros(1000)
y3 = np.zeros(1000)
for i in range(1000):
    y1[i] = Riemann_sum(np.sin, 0, x[i], 100)
    y2[i] = Riemann_integral(np.sin, 0, x[i], 100)
    y3[i] = integrate.quad(np.sin, 0, x[i])[0]
print("--- %s seconds ---" % (time.time() - start_time))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y1, y2, c='r', marker='o')
ax.scatter(x, y1, y3, c='b', marker='o')
ax.scatter(x, y2, y3, c='g', marker='o')
ax.set_xlabel('x')
ax.set_ylabel('y1')
ax.set_zlabel('y2')
plt.show()

# plot the Riemann sum in comparison to the Riemann integral and the scipy.integrate.quad function
plt.plot(x, y1, label='Riemann sum')
plt.plot(x, y2, label='Riemann integral')
plt.plot(x, y3, label='scipy.integrate.quad')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Riemann sum in comparison to the Riemann integral and the scipy.integrate.quad function')
plt.legend()
plt.show()
