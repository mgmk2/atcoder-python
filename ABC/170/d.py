from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
a.sort()
d = defaultdict(int)
for ai in a:
    d[ai] += 1

m = a[-1]
x = [True for _ in range(m + 1)]

ans = 0
c = defaultdict(bool)
for ai in a:
    if x[ai] and d[ai] == 1:
        ans += 1
    if not c[ai]:
        c[ai] = True
        for j in range(2 * ai, m + 1, ai):
            x[j] = False
print(ans)
