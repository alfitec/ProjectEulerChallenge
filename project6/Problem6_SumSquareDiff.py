"""
Sum square difference
   
Problem 6
The sum of the squares of the first ten natural numbers is,

1**2+2**2+...+10**2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)**2=552=3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum 
"""

#import profile as cp
import timeit

def brute(x):
    suma=sumSq=0
    for i in range(1,x+1):
        suma+=i
        sumSq+=i*i
    return suma**2-sumSq

def bruteFun(x):
    #brojevi=[i for i in range(1,x+1)]
    suma=sum(range(1,x+1))
    sumaSq=sum(map(lambda x:x**2,range(1,x+1)))
    return suma**2-sumaSq

def bruteMath(x):
    suma=(x+1)*x//2
    sumaSq= (((2*x+3)*x+1)*x)//6
    # See: https://en.wikipedia.org/wiki/Faulhaber%27s_formula
    return suma**2-sumaSq



print(brute(100))
print(timeit.timeit("brute(100)",setup="from __main__ import brute",number=100000))
print(bruteFun(100))
print(timeit.timeit("bruteFun(100)",setup="from __main__ import bruteFun",number=100000))
print(bruteMath(100))
print(timeit.timeit("bruteMath(100)",setup="from __main__ import bruteMath",number=100000))
