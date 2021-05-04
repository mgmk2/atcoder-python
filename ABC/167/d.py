n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0 for _ in range(n)]
p = 1
i = 0
while True:
    p = a[p - 1]
    if b[p - 1] > 0 or p == 1:
        break
    else:
        i += 1
        b[p - 1] = i
bp = b[p - 1]
if k <= bp:
    print(b.index(k) + 1)
else:
    l = bp + (k - bp) % (i + 1 - bp)
    print(b.index(l) + 1)
