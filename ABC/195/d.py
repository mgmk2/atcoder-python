import bisect

n, m, q = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(n)]
W.sort()

x = list(map(int, input().split()))

Q = [list(map(int, input().split())) for _ in range(q)]

for l, r in Q:
    y = set()
    ans = 0
    xq = x[:l - 1] + x[r:]
    xq.sort()
    for xi in xq:
        k = bisect.bisect_right(W, [xi, 10 ** 6 + 1])
        V = [[kk, *W[kk]] for kk in range(k) if kk not in y]
        if len(V) == 0:
            continue
        V.sort(key=lambda v: v[-1], reverse=True)
        ans += V[0][-1]
        y.add(V[0][0])
    print(ans)