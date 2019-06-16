n, x = map(int, input().split())
l = list(map(int, input().split()))
d = 0
for i, li in enumerate(l):
    d += li
    if d > x:
        print(i + 1)
        break
else:
    print(n + 1)
