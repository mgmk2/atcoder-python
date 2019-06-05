from collections import defaultdict

n, w = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    wi, vi = map(int, input().split())
    d[wi].append(vi)
for key in d.keys():
    di = d[key]
    di.sort(reverse=True)
    a = [0]
    for i in di:
        a.append(a[-1] + i)
    d[key] = a
keys = list(d.keys())
for i in range(4 - len(keys)):
    key = max(keys) + i + 1
    d[key] = [0]
    keys.append(key)
ans = 0
for i in range(min(w // keys[0] + 1, len(d[keys[0]]))):
    wi = w - keys[0] * i
    ai = d[keys[0]][i]
    for j in range(min(wi // keys[1] + 1, len(d[keys[1]]))):
        wj = wi - keys[1] * j
        aj = d[keys[1]][j]
        for k in range(min(wj // keys[2] + 1, len(d[keys[2]]))):
            wk = wj - keys[2] * k
            ak = d[keys[2]][k]
            idx = min(wk // keys[3], len(d[keys[3]]) - 1)
            ans = max(ans, ai + aj + ak + d[keys[3]][idx])
print(ans)
