def consolidateRows(prevRow,currentRow):
    nwRow1=(sum(z) for z in zip((0,*prevRow),currentRow))
    nwRow2=(sum(z) for z in zip((*prevRow,0),currentRow))
    return tuple(max(z) for z in zip(nwRow1,nwRow2))   # returning generators without converting to touple makes problems

#print(max(list(reduce(consolidateRows,triangle)))) 

from functools import reduce
import urllib.request

get_url= urllib.request.urlopen('https://projecteuler.net/project/resources/p067_triangle.txt')

print("Response Status: "+ str(get_url.getcode()) )
print(type(get_url))
data=get_url.read().decode('utf-8')
print(type(data))

data2=[[int(y) for y in x.split()] for x in data.split("\n")]
print(data2)
print(max(list(reduce(consolidateRows,data2[0:-1]))))