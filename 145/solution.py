counter=0
for i in range(1,1000000000):
    isreversed = True
    reverse = int(str(i)[::-1])
    temp = str(i+reverse)
    if str(i)[0]=='0' or str(i)[len(str(i))-1]=='0':
        isreversed=False
    for j in range(len(temp)):
        if(int(temp[j])%2==0):
            isreversed=False
            break
    if(isreversed):
        counter+=1
print(counter)
