import math
X = int(input())
Xr = int(math.sqrt(X))
ans = 1
for i in range(2, Xr + 1):
    t = i ** int(round(math.log(X, i), 10))
    if t > ans:
        ans = t
print(ans)
