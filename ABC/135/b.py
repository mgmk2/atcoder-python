n = int(input())
p = list(map(int, input().split()))
ps = sorted(p)
x = 0
for i, j in zip(p, ps):
    if i != j:
        x += 1
if x > 2:
    print('NO')
else:
    print('YES')
