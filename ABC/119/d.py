import bisect

a, b, q = map(int, input().split())
INF = 10 ** 11
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
x = [int(input()) for _ in range(q)]
s = [-INF] + s + [INF]
t = [-INF] + t + [INF]

ans = []
for xi in x:
    s_idx = bisect.bisect_left(s, xi)
    t_idx = bisect.bisect_left(t, xi)
    yi = []
    for j in range(2):
        sj = s[s_idx - j]
        for k in range(2):
            tk = t[t_idx - k]
            d = min(abs(xi - sj), abs(xi - tk)) + abs(sj - tk)
            yi.append(d)
    ans.append(min(yi))
for ansi in ans:
    print(ansi)
