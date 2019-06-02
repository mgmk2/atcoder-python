n, k = map(int, input().split())
ans = 0
if k == 0:
    ans = n ** 2
else:
    for b in range(k + 1, n):
        p = n // b
        r = n % b
        ans += p * max(0, b - k) + max(0, r - k + 1)
    ans += n - k
print(ans)
