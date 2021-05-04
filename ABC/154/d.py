n, k = map(int, input().split())
p = list(map(int, input().split()))
a = [0 for _ in range(n + 1)]
for i, pi in enumerate(p):
    a[i + 1] = a[i] + (1 + pi) / 2

ans = 0
for i in range(n - k + 1):
    ans = max(ans, a[i + k] - a[i])
print(ans)
