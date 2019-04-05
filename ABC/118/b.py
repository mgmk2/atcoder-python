n, m = map(int, input().split())
x = [0 for _ in range(m)]
for i in range(n):
    k, *a = list(map(int, input().split()))
    for j in range(k):
        x[a[j] - 1] += 1
ans = 0
for i in range(m):
    if x[i] == n:
        ans += 1
print(ans)
