import math
s = list(map(int, list(input())))
k = int(input())
for i in range(len(s)):
    n = 5.0e+15 * math.log10(s[i])
    if n >= math.log10(k):
        print(s[i])
        exit()
    else:
        k -= 10**n
