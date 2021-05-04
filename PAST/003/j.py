import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = [-1 for _ in range(m)]
d = [0 for _ in range(n)]
ai_pre = a[0]
d[0] = -ai_pre
ans[0] = 1
for i in range(1, m):
    ai = a[i]
    x = bisect.bisect(d, -ai)
    if x < n:
        ans[i] = x + 1
        d[x] = -ai
print(*ans, sep='\n')
