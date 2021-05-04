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

MOD = 10 ** 9 + 7
x, y = map(int, input().split())
m = 2 * x - y
n = 2 * y - x
if m < 0 or n < 0:
    ans = 0
elif m % 3 > 0 or n % 3 > 0:
    ans = 0
else:
    m = m // 3
    n = n // 3
    ans = combnk_mod(m + n, min(m, n), MOD)
print(ans)
