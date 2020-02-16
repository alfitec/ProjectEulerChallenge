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
    lista=[i for i in range(2,x+1)]
    for i in range(len(lista)):
        d=lista[i]
        if d==1:continue
        broj*=d
        for j in range(i,len(lista)):
            if lista[j]%d==0: lista[j]//=d
    return broj
