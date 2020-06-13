from math import factorial
curiousnums = []
for i in range(3,100000):
    total = 0
    strnum = str(i)
    for j in range(len(strnum)):
        total += factorial(int(strnum[j]))
    if(total==i):
        curiousnums.append(i)
print(sum(curiousnums))
