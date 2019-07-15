from collections import defaultdict

class permnk_mod(object):
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

    def permnk(self, n, k):
        if n < k:
            return 0
        return (self.x[n - k] * self.y[n]) % self.p

def dfs(i, V, E, k):
    MOD = 10 ** 9 + 7
    p = permnk_mod(k - 1, MOD)
    ans = k
    V[i] = 1
    S = [i]
    while(len(S) > 0):
        vi = S.pop()
        for j in E[vi]:
            if V[j] == 0:
                V[j] = 1
                S.append(j)
        if vi == i:
            ans *= p.permnk(k - 1, len(E[vi]))
        elif len(E[vi]) > 1:
            ans *= p.permnk(k - 2, len(E[vi]) - 1)
        ans %= MOD
    return ans

n, k = map(int, input().split())
E = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
V = [0] * (n + 1)
ans = dfs(1, V, E, k)
print(ans)
