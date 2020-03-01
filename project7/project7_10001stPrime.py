"""
10001st prime
   
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

def prime(number):
    primes=[]
    for i in range (2,number+1):
        i_is_prime=True
        sqroot=math.sqrt(i)
        for j in primes:
            if i%j==0:
                i_is_prime=False
                break
            if j>sqroot: break
        if i_is_prime:
            primes.append(i)
    return primes


def foo():
    return prime(1000000)




print(foo()[10000])