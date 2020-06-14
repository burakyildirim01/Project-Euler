divnum,i,value = 0,1,0
while(divnum<=500):
    temp = int((i*(i+1))/2)
    factors = []
    m = 1
    while m*m <= temp:
        if temp % m == 0:
            factors.append(m)
            if temp//m != m:
                factors.append(temp//m)
        m += 1
    divnum = len(factors)
    value = temp
    i+=1
print(value)
