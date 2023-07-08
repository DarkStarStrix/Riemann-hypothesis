# prime number theory make a function to calculate the number of primes less than or equal to x
from rsa.prime import is_prime


# In[ ]:


def number_of_primes_less_than_or_equal_to_x(x):
    # x is the input value
    # returns the number of primes less than or equal to x
    if x < 2:
        return 0
    else:
        return np.sum(np.array([is_prime(i) for i in range(2, x + 1)]))


# make a function to calculate the number of primes less than or equal to x
# plot the number of primes less than or equal to x in the interval [0, 1000] with 1000 points
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1000, 1000)
y = np.zeros(1000)
for i in range(1000):
    y[i] = number_of_primes_less_than_or_equal_to_x(x[i])

plt.plot(x, y, label='number of primes less than or equal to x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('number of primes less than or equal to x')
plt.legend()
plt.show()
