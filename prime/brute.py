"""
Prime number generator, usefull for many assignments
"""

import cProfile

def prime(number):
    primes=[]
    for i in range (2,number+1):
        i_is_prime=True
        for j in primes:
            if i%j==0:
                i_is_prime=False
                break
        if i_is_prime:
            primes.append(i)
    return primes


def foo():
    return prime(100000)



cProfile.run('foo()')