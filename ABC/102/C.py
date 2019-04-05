import numpy as np
N = int(input())
a = np.array(list(map(int, input().split())), dtype=int)
b = a - np.arange(1, N + 1)
b.sort()
if N % 2 == 0:
    bb = (b[N // 2 - 1] + b[N // 2]) // 2
else:
    bb = b[N // 2]
print(np.sum(np.abs(b - bb)))
