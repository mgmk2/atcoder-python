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
        return (self.x[n - k] * self.x[k] * self.y[n]) % self.p

h, w, a, b = map(int, input().split())
MOD = 10 ** 9 + 7
c = combnk_mod(h + w, MOD)
ans = 0
for i in range(b + 1, w + 1):
    ans += c.combnk(h - a + i - 2, i - 1) * c.combnk(a + w - i - 1, a - 1) % MOD
    ans %= MOD
print(ans)
