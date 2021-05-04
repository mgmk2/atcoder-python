from fractions import gcd

def factrize(n):
    b = []
    while n % 2 == 0:
        b.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            b.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        b.append(n)
    return b

a, b = map(int, input().split())
d = gcd(a, b)
p = factrize(d)
p_unique = set(p)
print(len(p_unique) + 1)
