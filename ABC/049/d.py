import sys
from collections import Counter

class UnionFind(object):
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        elif self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[y] = x
            self.rank[x] += 1

sys.setrecursionlimit(10 ** 5 + 1)

n, k, l = map(int, input().split())
Ur = UnionFind(n)
for i in range(k):
    p, q = map(int, input().split())
    Ur.union(p, q)

Ut = UnionFind(n)
for i in range(l):
    r, s = map(int, input().split())
    Ut.union(r, s)

x = [(Ur.find(i + 1), Ut.find(i + 1)) for i in range(n)]
c = Counter(x)
ans = []
for i in range(n):
    ans.append(c[x[i]])
print(' '.join([str(a) for a in ans]))
