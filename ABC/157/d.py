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
        if x != y:
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
        return self.member[self.find(x)]

n, m, k = map(int, input().split())
U = UnionFind(n)
may_friend = [-1 for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    U.union(a, b)
    may_friend[a] += -1
    may_friend[b] += -1
for i in range(k):
    c, d = map(int, input().split())
    if U.check(c, d):
        may_friend[c] += -1
        may_friend[d] += -1

ans = [max(0, may_friend[i] + U.size(i)) for i in range(1, n + 1)]
print(*ans)
