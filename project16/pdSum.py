pow=2**1000
sum=0
while pow:
    sum+=pow%10
    pow//=10
print(sum)