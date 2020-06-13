terms = []
total = 0
previous = 1
current = 2
terms.append(previous)
terms.append(current)
while current<4000000:
    nextnum = previous + current
    previous = current
    current = nextnum
    terms.append(current)
for i in range(len(terms)):
    if(terms[i]%2==0):
        total += terms[i]
print(total)
