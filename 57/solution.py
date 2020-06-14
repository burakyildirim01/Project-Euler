m,n,counter = 1,1,0
for i in range(1000):
    nom = m+2*n
    denom = m+n
    if(len(str(nom))>len(str(denom))):
        counter+=1
    m=nom
    n=denom
print(counter)
