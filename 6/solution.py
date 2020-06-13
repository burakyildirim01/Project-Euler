def calculatediff(n):
    return int(((n*(n+1))/2)**2 - (n*(n+1)*(2*n+1))/6)
    
print(calculatediff(100))
