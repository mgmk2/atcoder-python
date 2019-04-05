import numpy as np
h, w = map(int, input().split())
a = np.zeros([h, w], dtype=int)
idx_h = []
idx_w = []
for i in range(h):
    s = input()
    v = list(map(int, s.replace('.', '1 ').replace('#', '-1 ').split()))
    if sum(v) != w:
        a[i, :] = v
        idx_h.append(i)
aa = np.sum(a, axis=0)
for i in range(w):
    if aa[i] != len(idx_h):
        idx_w.append(i)
for i in idx_h:
    s = ''
    for j in idx_w:
        if a[i, j] == 1:
            s += '.'
        elif a[i, j] == -1:
            s += '#'
    print(s)
