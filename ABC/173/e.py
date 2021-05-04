from functools import reduce

MOD = 10 ** 9 + 7

n, k = map(int, input().split())
a = list(map(int, input().split()))
a_plus = [ai for ai in a if ai > 0]
b = [(abs(ai), ai >= 0) for ai in a]
b.sort(reverse=True)
c = [bi[0] for bi in b]
m = 0
xm0 = None
xm1 = None
x = []
for i in range(n):
    bi, p = b[i]
    if i < k:
        m += 1 - p
        xm0 = bi
    else:
        if not p and xm1 is None:
            xm1 = bi
        if p and len(x) < 2:
            x.append(bi)
ans = reduce(lambda a, b: (a % MOD) * (b % MOD) % MOD, c[:k])
if m % 2:
    xm = 0
    if xm0 is not None and xm1 is not None:
        xm = xm0 * xm1
    xx = 0
    if len(x) == 2:
        xx = x[0] * x[1]
    print(xm, xx)
    if xm > xx:
        ans *= pow(xm, MOD - 2, MOD)
        ans %= MOD
        ans *= xm
    else:
        ans *= pow(x[0], MOD - 2, MOD)
        ans %= MOD
        ans *= xx
print(ans)
