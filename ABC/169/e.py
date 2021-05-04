n = int(input())
a = [None for _ in range(n)]
b = [None for _ in range(n)]
for i in range(n):
    a[i], b[i] = map(int, input().split())
a.sort()
b.sort()

if n % 2:
    print(b[n // 2] - a[n // 2] + 1)
else:
    bb = b[n // 2] + b[n // 2 - 1]
    aa = a[n // 2] + a[n // 2 - 1]
    print(bb - aa + 1)
