class UnionFind(object):
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]
        self.member = [1 for i in range(n + 1)]

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
            self.member[y] += self.member[x]
        elif self.rank[x] > self.rank[y]:
            self.par[y] = x
            self.member[x] += self.member[y]
        else:
            self.par[y] = x
            self.rank[x] += 1
            self.member[x] += self.member[y]

    def size(self, x):
        return self.member[self.par[x]]

n, m = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(m)]
ans = [0 for _ in range(m + 1)]
ans[-1] = n * (n - 1) // 2
tree = UnionFind(n)
for i, e in enumerate(E[::-1]):
    if tree.check(*e):
        ans[-(i + 2)] = ans[-(i + 1)]
    else:
        ans[-(i + 2)] = ans[-(i + 1)] -  tree.size(e[0]) * tree.size(e[1])
        tree.union(*e)
for a in ans[1:]:
    print(a)
