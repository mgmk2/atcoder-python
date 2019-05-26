import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
c = [None] * m
for j in range(m):
    c[j] = list(map(int, input().split()))
c.sort(key=lambda x: x[1], reverse=True)
k = 0
ans = 0
for i in range(n):
    if k >= m:
        ans += sum(a[i:])
        break
    if a[i] >= c[k][1]:
        ans += a[i]
    else:
        ans += c[k][1]
        c[k][0] -= 1
        if c[k][0] == 0:
            k += 1
print(ans)
