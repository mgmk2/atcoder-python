def divisors(n):
    x = set()
    m = 1
    while m * m <= n:
        if n % m == 0:
            x.add(m)
            x.add(n // m)
        m += 1
    return x

n = int(input())
d = divisors(n)
ans = 0
for k in d:
    if k == 1:
        continue
    nn = n
    while nn % k == 0:
        nn = nn // k
    ans += nn % k == 1

d1 = divisors(n - 1)
ans += len(d1) - 1
print(ans)
