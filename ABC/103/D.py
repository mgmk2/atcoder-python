import numpy as np
N, M = map(int, input().split())
a = np.zeros([M], dtype=int)
b = np.zeros([M], dtype=int)
for i in range(M):
    a[i], b[i] = map(int, input().split())
idx = np.argsort(b)
a = a[idx]
b = b[idx]
c = b[0] - 1
ans = 1
for i in range(1, M):
    if a[i] <= c:
        continue
    else:
        c = b[i] - 1
        ans += 1
print(ans)
