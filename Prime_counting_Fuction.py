# make a prime counting function that counts the number of primes between 2 and n and plots the number of primes as a function of n

import numpy as np
import matplotlib.pyplot as plt


def prime_counting_function(n):
    # make an array of all the numbers between 2 and n
    numbers = np.arange(2, n + 1)
    # make an array of all the numbers between 2 and n that are not divisible by any number between 2 and n
    primes = []
    for i in numbers:
        if i == 2:
            primes.append(i)
        else:
            for j in range(2, i):
                if i % j == 0:
                    break
                elif j == i - 1:
                    primes.append(i)
    return len(primes)


# make an array of all the numbers between 2 and 1000
n = np.arange(2, 1001)
# make an array of the number of primes between 2 and n
prime_count = []
for i in n:
    prime_count.append(prime_counting_function(i))

# plot the number of primes as a function of n
plt.plot(n, prime_count)
plt.xlabel('n')
plt.ylabel('Number of Primes')
plt.title('Number of Primes as a Function of n')
plt.show()

# plot the number of primes as a function of n on a log-log scale
plt.loglog(n, prime_count)
plt.xlabel('n')
plt.ylabel('Number of Primes')
plt.title('Number of Primes as a Function of n')
plt.show()


# code Gauss's conjecture that the number of primes less than or equal to n is approximately n/ln(n)
# make a function that calculates the number of primes less than or equal to n
def prime_counting_function_approx(n):
    return n / np.log(n)


# make an array of the number of primes less than or equal to n
prime_count_approx = []
for i in n:
    prime_count_approx.append(prime_counting_function_approx(i))

# plot the number of primes as a function of n and the approximation of the number of primes as a function of n
plt.plot(n, prime_count, label='Number of Primes')
plt.plot(n, prime_count_approx, label='Approximation of Number of Primes')
plt.xlabel('n')
plt.ylabel('Number of Primes')
plt.title('Number of Primes as a Function of n')
plt.legend()
plt.show()
