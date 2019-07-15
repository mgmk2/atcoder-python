class combnk_mod(object):
    # pが素数かつaとpが互いに素であるとき
    # フェルマーの小定理より以下が成り立つ.
    # 1 / a = a ** (p - 2) (mod p)
    # これを使って (1 / k!) mod p を計算する.
    def __init__(self, maxn, p):
        self.maxn = maxn
        self.p = p
        self.x = [1] # 分母にあたる数 1 / n! mod p
        self.y = [1] # 分子にあたる数. n! mod p
        for i in range(1, self.maxn + 1):
            self.x.append(self.x[-1] * pow(i, self.p - 2, self.p) % self.p)
            self.y.append(self.y[-1] * i % self.p)

    def combnk(self, n, k):
        if n < k:
            return 0
        return (self.x[n - k] * self.x[k] * self.y[n]) % self.p

n, k = map(int, input().split())
MOD = 10 ** 9 + 7
c = combnk_mod(n, MOD)
for i in range(1, k + 1):
    ans = c.combnk(n - k + 1, i) * c.combnk(k - 1, i - 1)
    print(ans % MOD)
