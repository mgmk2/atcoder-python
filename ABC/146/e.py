n, k = map(int, input().split())
a = list(map(int, input().split()))
s = [0 for _ in range(n + 1)]
for i in range(n):
    s[i + 1] = s[i] + a[i]

ans = 0
for i, si in enumerate(s[:-1]):
    for j in range(i, min(i + k, n)):
        if (s[j + 1] - si) % k == j - i + 1:
            ans += 1
print(ans)
