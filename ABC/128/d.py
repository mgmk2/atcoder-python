n, k = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
if n == 1:
    ans = max(0, v[0])
else:
    ans = 0 if k < n else sum(v)
    for i in range(min(k + 1, n)):
        for j in range(i + 1):
            t = v[:j]
            if j != i:
                t += v[j - i:]
            t.sort()
            for p in range(k - i):
                if len(t) > 0 and t[0] < 0:
                    t.pop(0)
                else:
                    break
            if len(t) == 0:
                t = [0]
            ans = max(ans, sum(t))
print(ans)
