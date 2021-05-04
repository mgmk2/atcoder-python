n, k = map(int, input().split())
x = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    if x[i] > 0:
        continue
    for j in range(i, n + 1, i):
        x[j] += 1
ans = 0
for i in x:
    if i >= k:
        ans += 1
print(ans)
