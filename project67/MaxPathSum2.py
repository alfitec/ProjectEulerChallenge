def consolidateRows(prevRow,currentRow):
    return tuple(   max(z[0],z[2])+z[1]     for z in zip(  (0,*prevRow),  currentRow,  (*prevRow,0)  )  )  
    # returning generators without converting to touple makes problems

import urllib.request

"""
with urllib.request.urlopen('https://projecteuler.net/project/resources/p067_triangle.txt') as response:
    data=response.read().decode('utf-8')
    triangle=[[int(y) for y in x.split()] for x in data.split("\n") if x]
"""

with open('project67/p067_triangle.txt') as triangle_file:
    data=triangle_file.read()
    triangle=[[int(y) for y in x.split()] for x in data.split("\n") if x]

from functools import reduce
print(max(list(reduce(consolidateRows,triangle))))