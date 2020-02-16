"""
Smallest multiple
   
Problem 5
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def NZS(x):
    deljiv=False
    broj=1
    while(not deljiv):
        deljiv=True
        for i in range(2,x+1):
            if broj%i != 0:
                deljiv=False
                break;
        if deljiv: break;
        broj+=1
    return broj