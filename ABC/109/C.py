from fractions import gcd
import numpy as np
n, x0 = map(int, input().split())
x = np.abs(np.array(list(map(int, input().split()))) - x0)
xx = x[0]
for i in range(1, n):
    xx = gcd(xx, x[i])
print(xx)
