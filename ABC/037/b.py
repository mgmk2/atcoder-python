n, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(q)]
x = [0] * n
for l, r, t in a:
    for i in range(l - 1, r):
        x[i] = t
for ans in x:
    print(ans)
