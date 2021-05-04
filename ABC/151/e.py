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
a = list(map(int, input().split()))
a.sort()
MOD = 10 ** 9 + 7
combnk = combnk_mod(n, MOD)
ans = 0
if k == 1:
    print(0)
else:
    x = [0 for _ in range(n)]
    y = [combnk.combnk(i, k - 2) for i in range(n + 1)]
    ya = [0]
    for yi in y:
        ya.append(ya[-1] + yi)

    for i in range(n):
        x[i] = ya[i] - ya[max(0, n - i - 1)]
    for xi, ai in zip(x, a):
        ans += xi * ai % MOD
        ans %= MOD
    print(ans)
