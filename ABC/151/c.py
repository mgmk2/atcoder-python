n, m = map(int, input().split())
d = [False for _ in range(n)]
x = [0 for _ in range(n)]
penalty = 0
for i in range(m):
    p, s = input().split()
    p = int(p) - 1
    if d[p]:
        continue
    if s == 'AC':
        d[p] = True
        penalty += x[p]
    else:
        x[p] += 1

print(sum(d), penalty)
