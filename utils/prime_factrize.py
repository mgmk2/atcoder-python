def prime_factrize(n):
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
