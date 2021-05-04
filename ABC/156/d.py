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

if __name__ == '__main__':
    MOD = 10 ** 9 + 7
    n, a, b = map(int, input().split())
    ans = pow(2, n, MOD) - 1
    ans %= MOD
    for k in [a, b]:
        ans -= combnk_mod(n, k, MOD)
        ans %= MOD
    print(ans)
