chainsizes=[]
numsglobal=[]
for n in range(1,1000000):
    numbers = []
    numbers.append(n)
    while(n!=1):
        if(n%2==0):
            n = int(n/2)
            numbers.append(n)
        else:
            n = 3*n+1
            numbers.append(n)
    numsglobal.append(numbers)
    chainsizes.append(len(numbers))
print(numsglobal[chainsizes.index(max(chainsizes))][0])
