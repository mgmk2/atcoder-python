from collections import Counter

w = input()
c = Counter(list(w))
ans = True
for v in c.values():
    if v % 2:
        ans = False
        break
if ans:
    print('Yes')
else:
    print('No')
