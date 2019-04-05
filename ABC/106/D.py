import numpy as np
N, M, Q = map(int, input().split())
x = np.zeros([N, N], dtype=int)
y = np.zeros([N, N], dtype=int)
for m in range(M):
    L, R = map(int, input().split())
    x[L-1, R-1] += 1
for i in range(N):
    y[i, :] = np.sum(x[:i+1, :], axis=0)
for i in range(Q):
    p, q = map(int, input().split())
    if p == 1:
        print(np.sum(y[q-1, p-1:q]))
    else:
        print(np.sum(y[q-1, p-1:q] - y[p-2, p-1:q]))
