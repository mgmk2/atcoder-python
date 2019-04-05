def argmax_taste(t, d, tt):
    xx = 0
    ans = 0
    lt = len(tt)
    for i, di in enumerate(d):
        if t[i] in tt.keys():
            ti = 0
        else:
            ti = 2 * lt + 1
        if di + ti > xx:
            xx = di + ti
            ans = i
    return ans, xx

n, k = map(int, input().split())
t = [None for _ in range(n)]
d = [None for _ in range(n)]
for i in range(n):
    t[i], d[i] = map(int, input().split())

tt = {}
ans = 0
for i in range(k):
    j, tmp = argmax_taste(t, d, tt)
    ans += tmp
    tt[t[j]] = None
    del d[j], t[j]
print(ans)
