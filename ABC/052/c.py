def prime(x):
    y = list(range(1, x + 1))
    y[0] = 0
    x_sqrt = x ** 0.5
    for i in y:
        if i > x_sqrt:
            break
        elif i == 0:
            continue
        for not_prime in range(2 * i, x + 1, i):
            y[not_prime - 1] = 0
    return [i for i in y if i > 0]

n = int(input())
MOD = 10 ** 9 + 7
primes = prime(n)
m = [0 for _ in range(len(primes))]
for i, p in enumerate(primes):
    for j in range(1, n + 1):
        while(j % p == 0):
            m[i] += 1
            j = j // p
ans = 1
for i in m:
    ans *= (i + 1)
    ans = ans % MOD
print(ans)
