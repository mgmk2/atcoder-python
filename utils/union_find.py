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
