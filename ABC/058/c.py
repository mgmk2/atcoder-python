n = int(input())
s0 = input()
d = {}
for sk in s0:
    if sk in d.keys():
        d[sk] += 1
    else:
        d[sk] = 1

for i in range(1, n):
    si = input()
    for key in d.keys():
        if d[key] == 0:
            continue
        x = si.count(key)
        if x < d[key]:
            d[key] = x
ans = []
for key, sk in d.items():
    for _ in range(sk):
        ans.append(key)
ans.sort()
print(''.join(ans))
