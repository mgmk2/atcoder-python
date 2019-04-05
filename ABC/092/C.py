n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]
ans = []
i = 1
s = [abs(a[1])] + [None for _ in range(n)]
d = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    s[i] = abs(a[i + 1] - a[i])
    if (a[i - 1] - a[i]) * (a[i] - a[i + 1]) >= 0:
        d[i] = 0
    else:
        d[i] = s[i] + s[i - 1] - abs(a[i + 1] - a[i - 1])
ss = sum(s)
for i in range(1, n + 1):
    print(ss - d[i])
