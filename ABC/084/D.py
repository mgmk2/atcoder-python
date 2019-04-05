import numpy as np
a = np.arange(1, 100001)
t = np.ones([len(a)], dtype=bool)
for i in range(1, 50000):
    t[i + a[i]::a[i]] = False
t[0] = False
s = [0, 0]
for i in range(2, 100000):
    if i % 2:
        s.append(s[-1])
    else:
        if t[i] and t[(i + 2) // 2 - 1]:
            s.append(s[-1] + 1)
        else:
            s.append(s[-1])
Q = int(input())
ans = []
for i in range(Q):
    L, R = map(int, input().split())
    if L == 1:
        ans.append(s[R - 1])
    else:
        ans.append(s[R - 1] - s[L - 2])
for i in range(Q):
    print(ans[i])
