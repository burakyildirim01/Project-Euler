counter=0
for i in range(1,10):
    power=1
    while(True):
        if(power == len(str(pow(i,power)))):
            counter += 1
        else:
            break
        power+=1
print(counter)
