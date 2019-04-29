n, m = map(int, input().split())
d = dict.fromkeys(list(range(1, n + 1)), 0)
for i in range(m):
    a, b = map(int, input().split())
    d[a] += 1
    d[b] += 1
for i in range(1, n + 1):
    print(d[i])
