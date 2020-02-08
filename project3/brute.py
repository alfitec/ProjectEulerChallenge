"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number  ?
"""
# I ovo je komentar
import math

def largestPrime(num):
    bigestPrime,currentPrime=1,2
    #print(bigestPrime,currentPrime,num)
    broj=num
    sqrtBroj=math.sqrt(broj)+1
    #while(currentPrime*currentPrime<num)
    while(currentPrime<=broj):
        if broj%currentPrime==0:
            #print("delim sa: ", currentPrime)
            bigestPrime=currentPrime
            broj=broj//currentPrime
            sqrBroj=math.sqrt(broj)+1
            print("delim sa: ", currentPrime, " dobijam: ",broj)
        else:
            currentPrime+=1
            if currentPrime>sqrtBroj:
                currentPrime=broj
    return bigestPrime


print("rezultat je",largestPrime(600851475143))
print("rezultat je",largestPrime(1000000007))