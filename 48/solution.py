total = 0
result = ""
for i in range(1,1001):
    total += pow(i,i)
for i in range(10):
    remainder = total % 10
    result += str(remainder)
    total //= 10
print(result[::-1])
