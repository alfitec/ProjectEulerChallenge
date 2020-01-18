"""
Project Euler: Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
"""


def multiples(number):
    sum=0
    for i in range(1,number):    # if we wont to include number in sum we can put number+1 here
        if i%3==0 or i%5==0:
            sum+=i
    return sum


print(multiples(10))
print(multiples(1000))
print(multiples(49))
print(multiples(19564))
print(multiples(10000))
print(multiples(8456))
print(multiples(3))
print(multiples(5))

"""
multiplesOf3and5(1000) should return 233168.
multiplesOf3and5(49) should return 543.
multiplesOf3and5(19564) should return 89301183.
multiplesOf3and5(8456) should return 16687353.
"""