def calculatediff(n):
    return sum(i for i in range(n+1))**2-sum(i**2 for i in range(n+1))
    
print(calculatediff(100))
