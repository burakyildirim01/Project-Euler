from fractions import gcd
arr = []
for i in range(1,21):
    arr.append(i)
lcm = arr[0]
for i in arr[1:]:
  lcm = int(lcm*i/gcd(lcm, i))
print(lcm)
