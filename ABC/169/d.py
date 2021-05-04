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

n = int(input())
d = prime_factrize(n)
ans = 0
for x in d.values():
    y = 0
    for k in range(1, x + 1):
        y += k
        if y + k >= x:
            break
    ans += k
print(ans)
