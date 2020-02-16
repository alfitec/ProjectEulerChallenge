"""
Smallest multiple
   
Problem 5
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def NZD(x,y):
    if x<y: return NZD(y,x)
    res=x%y
    if res>0: return NZD(y,res)
    else: return y
    
    
    
    
def NZS(x):
    deljiv=False
    broj=1
    for i in range(x,2,-1):
        nzd=NZD(broj,i)
        if nzd!=i:broj*=i//nzd
            
    return broj
