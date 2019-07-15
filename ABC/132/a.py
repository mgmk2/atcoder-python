from collections import defaultdict

s = input()
d = defaultdict(int)
for si in s:
    d[si] += 1
if len(d.keys()) == 2 and list(d.values()) == [2, 2]:
    print('Yes')
else:
    print('No')
