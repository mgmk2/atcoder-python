from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

posd = defaultdict(list)
for i, ai in enumerate(a):
    posd[ai].append(i + 1)

for k in posd.keys():
    posd[k].sort()

ans = n
for i in range(n):
    if len(posd[i]) == 0:
        ans = i
        break
    
    pre = 0
    for v in posd[i]:
        if v - pre > m:
            break
        pre = v
    else:
        if n + 1 - posd[i][-1] <= m:
            continue
    ans = i
    break

print(ans)