maxnum=0
for a in range(1,101):
    for b in range(1,101):
        maxnum = max(maxnum,sum(map(int, str(pow(a, b)))))
print(maxnum)
