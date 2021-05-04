n = int(input())
s = input()
res = [[None for j in range(10)] for i in range(n)]
res[-1][int(s[-1])] = n - 1
for i in range(n - 2, -1, -1):
    for j in range(10):
        res[i][j] = res[i + 1][j]
    res[i][int(s[i])] = i
ans = 0
for i in range(10):
    x = res[0][i]
    if x is None or x > n - 3:
        continue
    for j in range(10):
        y = res[x + 1][j]
        if y is None or y > n - 2:
            continue
        for k in range(10):
            z = res[y + 1][k]
            if z is not None:
                ans += 1
print(ans)
