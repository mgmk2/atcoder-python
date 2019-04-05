import numpy as np
N = int(input())
X = np.array(list(map(int, input().split())), dtype=int)
idx = np.argsort(X)
Xs = X[idx]
ans = [None for _ in range(N)]
for i in range(N // 2):
    ans[idx[i]] = Xs[N // 2]
for i in range(N // 2, N):
    ans[idx[i]] = Xs[N // 2 - 1]
for i in range(N):
    print(ans[i])
