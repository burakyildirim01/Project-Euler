from math import sqrt
from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def findlargestprimefac(n):
    factors = []
    primefactors = []
    m = 1
    while m*m <= n:
        if n % m == 0:
            factors.append(m)
            if n//m != m:
                factors.append(n//m)
        m += 1
    for i in range(len(factors)):
        if(isPrime(factors[i])):
            primefactors.append(factors[i])
    return(max(primefactors))
    
print(findlargestprimefac(600851475143))
