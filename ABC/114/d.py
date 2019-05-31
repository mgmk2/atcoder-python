from collections import defaultdict

n = int(input())
x = defaultdict(int)
for i in range(2, n + 1):
    k = i
    for j in range(2, i + 1):
        while(k % j == 0):
            k = k // j
            x[j] += 1

y = defaultdict(int)
for i in x.values():
    for j in [2, 4, 14, 24, 74]:
        if i >= j:
            y[j] += 1

ans = 0
ans += y[4] * max(0, y[4] - 1) * max(0, y[2] - 2) // 2
ans += y[14] * max(0, y[4] - 1)
ans += y[24] * max(0, y[2] - 1)
ans += y[74]
print(ans)
