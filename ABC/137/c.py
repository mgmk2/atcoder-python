from collections import defaultdict

n = int(input())
d = defaultdict(int)
for i in range(n):
    s = input()
    ss = ''.join(sorted(s))
    d[ss] += 1

ans = 0
for v in d.values():
    ans += v * (v - 1) // 2
print(ans)
