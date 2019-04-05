n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    if a[i] in d:
        d[a[i]] += 1
    else:
        d[a[i]] = 1
ans = 0
for i in d:
    if d[i] < i:
        ans += d[i]
    if d[i] > i:
        ans += d[i] - i
print(ans)
