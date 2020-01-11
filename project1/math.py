"""
Project Euler: Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
"""


def multiples(number):
    sum=0
    divisibleBy3=number/3
    divisibleBy5=number/5
    divisibleBy15=number/15
    sum= 3* (divisibleBy3*(divisibleBy3+1)/2) + \
         5* (divisibleBy5*(divisibleBy5+1)/2) - \
        15* (divisibleBy15*(divisibleBy15+1)/2)
    return sum


print(multiples(1000))
print(multiples(49))
print(multiples(19564))
print(multiples(100000000000))
print(multiples(8456))

"""
multiplesOf3and5(1000) should return 233168.
multiplesOf3and5(49) should return 543.
multiplesOf3and5(19564) should return 89301183.
multiplesOf3and5(8456) should return 16687353.
"""