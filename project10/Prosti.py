import math
def brute():
    prosti=[]
    zbir=0
    for i in range(2,2000001):
        deljiv=False
        j2=int(math.sqrt(i))+1
        for j in prosti:
            if (j>j2):break
            if (i%j==0):
                deljiv=True
                break
        if (not deljiv):
            prosti.append(i)
            zbir+=i
           # print(i)
        if (i%10000==0): print(i)
    return zbir