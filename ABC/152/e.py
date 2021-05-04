from collections import defaultdict

def prime_factrize(n):
    b = defaultdict(int)
    while n % 2 == 0:
        b[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            b[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        b[n] += 1
    return b

def lcm_prime(a, b):
    keys = list(set(list(a.keys()) + list(b.keys())))
    d = defaultdict(int)
    for k in keys:
        d[k] = max(a[k], b[k])
    return d

MOD = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))
a_prime = [None for _ in range(len(a))]
l_prime = defaultdict(int)

for i, ai in enumerate(a):
    a_prime[i] = prime_factrize(ai)
    l_prime = lcm_prime(l_prime, a_prime[i])

print(l_prime)

ans = 0
for ai in a_prime:
    x = 1
    for p, lp in l_prime.items():
        x *= pow(p, lp - ai[p], MOD)
        x %= MOD
    ans += x
    ans %= MOD
print(ans)
