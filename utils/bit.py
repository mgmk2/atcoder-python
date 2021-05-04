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
