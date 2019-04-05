n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))
v0 = 0
s = [0] * n
for i in range(n):
    if i < n - 1:
        v1 = v[i + 1]
    else:
        v1 = 0
    x = max(0, min(t[i], (v1 - v0 + t[i]) / 2))
    if x + v0 > v[i]:
        x2 = min(t[i], v1 - v[i] + t[i])
        s[i] += (v[i] + v0) * (v[i] - v0) / 2
        s[i] += (x2 - v[i] + v0) * v[i]
        s[i] += (v[i] + v1) * (t[i] - x2) / 2
    else:
        s[i] += (2 * v0 + x) * x / 2
        s[i] += (v0 + x + v1) * (t[i] - x) / 2
    v0 = min(v[i], v1, v0 + t[i])
print(sum(s))
