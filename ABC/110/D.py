from collections import defaultdict

def combnk_mod(n, k, p):
    # pが素数かつaとpが互いに素であるとき
    # フェルマーの小定理より以下が成り立つ.
    # 1 / a = a ** (p - 2) (mod p)
    # これを使って (1 / k!) mod p を計算する.

    if  2 * k > n:
        k = n - k
    x = 1 # 分母にあたる数 1 / n! mod p
    y = 1 # 分子にあたる数. n! / (n - k)! mod p
    for i in range(1, k + 1):
        x *= pow(i, p - 2, p)
        y *= n - i + 1
        x %= p
        y %= p
    return (x * y) % p

n, m = map(int, input().split())
MOD = 10 ** 9 + 7
d = defaultdict(int)

for i in range(2, int(m ** 0.5) + 1):
    while(m % i == 0):
        m = m // i
        d[i] += 1
if m > 1:
    d[m] = 1

ans = 1
for i in d.values():
    ans *= combnk_mod(i + n - 1, i, MOD)
    ans %= MOD
print(ans)
