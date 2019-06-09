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

n, m = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(m)]
E.sort(reverse=True, key=lambda x: x[-1])
q = int(input())
question = [[i] + list(map(int, input().split())) for i in range(q)]
question.sort(key=lambda x: x[-1])
union = UnionFind(n)
ans = [None] * q
j = 0
for ai, bi, yi in E:
    while(j < q and question[-1][-1] >= yi):
        k, vk, _ = question.pop()
        ans[k] = union.size(vk)
        j += 1
    if j == q:
        break
    union.union(ai, bi)
else:
    while(j < q):
        k, vk, _ = question.pop()
        ans[k] = union.size(vk)
        j += 1
for i in range(q):
    print(ans[i])
