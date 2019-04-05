n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
d = {}
x = [0, 0]
k = 0
for ai in a:
    if ai in d:
        d[ai] += 1
    else:
        d[ai] = 1
    if d[ai] == 2 or d[ai] == 4:
        x[k] = ai
        k += 1
    if k == 2:
        break
print(x[0] * x[1])
