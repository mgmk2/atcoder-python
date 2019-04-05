n = int(input())
c = [None for _ in range(n - 1)]
s = [None for _ in range(n - 1)]
f = [None for _ in range(n - 1)]
for i in range(n - 1):
    c[i], s[i], f[i] = map(int, input().split())
for i in range(n - 1):
    t = 0
    for j in range(i, n - 1):
        if t < s[j]:
            t = s[j] + c[j]
        elif t % f[j] == 0:
            t += c[j]
        else:
            t += f[j] - t % f[j] + c[j]
    print(t)
print(0)
