n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
ans = h[-1]
for i in range(n - k + 1):
    x = h[i + k - 1] - h[i]
    if x < ans:
        ans = x
print(ans)
