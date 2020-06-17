from math import sqrt
from itertools import count, islice
total=0
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
for i in range(2000000):
    if(isPrime(i)):
        total+=i
print(total)
