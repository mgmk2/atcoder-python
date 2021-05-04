class BIT(object):
    def __init__(self, N, init=0, mod=1):
        self.N = N
        self.bit = [init for _ in range(N)]
        self.mod = mod

    def add(self, k, w):
        x = k
        while x < self.N:
            self.bit[x] += w % self.mod
            self.bit[x] %= self.mod
            x |= x + 1

    def sum(self, k):
        s = 0
        x = k - 1
        while x >= 0:
            s += self.bit[x]
            s %= self.mod
            x = (x & (x + 1)) - 1
        return s

MOD = 998244353
n, k = map(int, input().split())
seg = [list(map(int, input().split())) for _ in range(k)]
bit = BIT(n, mod=MOD)
bit.add(0, 1)

for i in range(1, n):
    x = 0
    for l, r in seg:
        x += (bit.sum(max(0, i - l + 1)) - bit.sum(max(0, i - r))) % MOD
        x %= MOD
    bit.add(i, x)
print((bit.sum(n) - bit.sum(n - 1)) % MOD)
