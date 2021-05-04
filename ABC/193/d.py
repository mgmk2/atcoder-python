from collections import defaultdict

k = int(input())
s = list(map(int, list(input()[:4])))
t = list(map(int, list(input()[:4])))

cs = [0 for _ in range(10)]
ct = [0 for _ in range(10)]
c = [0 for _ in range(10)]
for si in s:
    cs[si] += 1
    c[si] += 1
for ti in t:
    ct[ti] += 1
    c[ti] += 1

ps = sum([i * 10 ** v for i, v in enumerate(cs)])
pt = sum([i * 10 ** v for i, v in enumerate(ct)])

ws = 0
total = 0
for i in range(1, 10):
    if c[i] == k:
        continue
    psi = ps + i * 9 * 10 ** cs[i]
    for j in range(1, 10):
        if i == j and c[i] >= k - 1:
            continue
        if c[j] == k:
            continue
        ptj = pt + j * 9 * 10 ** ct[j]

        x = (k - c[i]) * (k - c[i] - 1) if i == j else (k - c[i]) * (k - c[j])
        if psi > ptj:
            ws += x
        total += x
print(ws / total)