import sys, time
from collections import defaultdict

sys.setrecursionlimit(10 ** 5 + 1)

def dfs(i, V, E, num):
    V[i] = num
    for j in [x for x in E[i] if V[x] == 0]:
        if V[j] > 0:
            continue
        V = dfs(j, V, E, num)
    return V

n, k, l = map(int, input().split())
Er = defaultdict(list)
for i in range(k):
    p, q = map(int, input().split())
    Er[p].append(q)
    Er[q].append(p)
Et = defaultdict(list)
for i in range(l):
    r, s = map(int, input().split())
    Et[r].append(s)
    Et[s].append(r)

start = time.time()
Vr_group = [None]
Vr = [0 for _ in range(n + 1)]
j = 1
for i in range(1, n + 1):
    if Vr[i] > 0:
        continue
    Vr = dfs(i, Vr, Er, j)
    Vr_group.append({t for t in range(1, n + 1) if Vr[t] == j})
    j += 1
print(time.time() - start)

start = time.time()
Vt_group = [None]
Vt = [0 for _ in range(n + 1)]
j = 1
for i in range(1, n + 1):
    if Vt[i] > 0:
        continue
    Vt = dfs(i, Vt, Et, j)
    Vt_group.append({t for t in range(1, n + 1) if Vt[t] == j})
    j += 1
print(time.time() - start)

start = time.time()
W = [[0 for j in range(len(Vt_group))] for i in range(len(Vr_group))]
for i in range(1, len(Vr_group)):
    for j in range(1, len(Vt_group)):
        W[i][j] = len(Vr_group[i] & Vt_group[j])
ans = []
for i in range(1, n + 1):
    ans.append(W[Vr[i]][Vt[i]])
print(time.time() - start)
print(' '.join([str(x) for x in ans]))
