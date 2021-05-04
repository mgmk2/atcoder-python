from bisect import bisect_right

n, d, a = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(n)]
m.sort()
x = [mm[0] for mm in m]
h = [mm[1] for mm in m]
y = [None for _ in range(n)]
idx = 0
ans = 0
hh = [0 for _ in range(n)]
for i in range(n):
    k = -((hh[i] - h[i]) // a)
    if k < 0:
        continue
    ans += k
    y = bisect_right(x, x[i] + 2 * d, lo=i)
    for j in range(i, y):
        hh[j] += k * a
print(ans)
