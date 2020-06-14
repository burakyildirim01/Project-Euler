result = 0
for i in range(2,200001):
    numstr = str(i)
    total = 0
    for a in range(len(numstr)):
        total += pow(int(numstr[a]),5)
    if(i==total):
        result += i
print(result)
