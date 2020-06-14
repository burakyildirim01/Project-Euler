def fibo(n):
    prev,curr = 1,1
    for i in range(n):
        prev,curr = curr,prev+curr
    return curr
length,i = 0,1
while(length!=1000):
    length = len(str(fibo(i)))
    i+=1
print(i+1)
