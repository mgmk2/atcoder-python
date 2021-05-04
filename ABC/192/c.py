n, k = map(int, input().split())
x = n
for i in range(k):
    g2 = ''.join(sorted(str(x)))
    g1 = g2[::-1]
    x = int(g1) - int(g2)
print(x)