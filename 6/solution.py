def calculatediff(n):
    return int(((n*(n+1))/2)**2 - (n*(n+1)*(2*n+1))/6)
    
print(calculatediff(100))
''' alternate solution
def calculatediff(n):
    return sum(i for i in range(n+1))**2-sum(i**2 for i in range(n+1))
    
print(calculatediff(100))
'''
