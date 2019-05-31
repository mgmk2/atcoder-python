class UnionFind(object):
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def check(self, x, y):
        return self.find(x) == self.find(y)

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

n, m = map(int, input().split())
p = list(map(int, input().split()))
tree = UnionFind(n)
for i in range(m):
    x, y = map(int, input().split())
    tree.union(x, y)
ans = 0
for i, pi in enumerate(p):
    if tree.check(i + 1, pi):
        ans += 1
print(ans)
