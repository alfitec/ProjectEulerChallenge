def fSum(num):
    f=1
    for i in range(1,num+1): f*=i
 
    s=0
    while(f):
        f,k=divmod(f,10)
        s+=k

    return s

    
print(fSum(100))