import itertools

s = input()
l = len(s)
ans = int(s)
for i in range(1, l):
    x = list(itertools.combinations(list(range(1, l)), i))
    for xi in x:
        p = 0
        for q in xi:
            ans += int(s[p:q])
            p = q
        ans += int(s[q:])
print(ans)
