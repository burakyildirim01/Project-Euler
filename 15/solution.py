from math import factorial
def findnumofpaths(n):
    return int((factorial(n+n))/(factorial(n)*factorial(n)))
print(findnumofpaths(20))
