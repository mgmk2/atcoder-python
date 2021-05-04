from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
C = Counter(s)
L = C.most_common()
x = 0
ans = []
for i, l in enumerate(L):
    if i == 0:
        x = l[1]
        ans.append(l[0])
    elif x == l[1]:
        ans.append(l[0])
    else:
        break
ans.sort()
for a in ans:
    print(a)
