from collections import defaultdict

n = int(input())
z = [list(map(int, input().split())) for _ in range(n)]
if n == 1:
    ans = 1
else:
    d = defaultdict(int)
    for i in range(n):
        xi, yi = z[i]
        for j in range(n):
            if i == j:
                continue
            xj, yj = z[j]
            d[(xi - xj, yi - yj)] += 1
    ans = n - max(d.values())
print(ans)
