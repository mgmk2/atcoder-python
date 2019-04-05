n, k = map(int, input().split())
ans = 0
if k == 0:
    ans = n
else:
    for i in range(n - k):
        b = k + i + 1
        p = n // b
        r = n % b
        ans += p * max(0, b - k) + max(0, r - k + 1) - 1
print(ans)
