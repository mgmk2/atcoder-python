n = int(input())
q = int(input())
s = [list(map(int, input().split())) for _ in range(q)]
rows = list(range(n))
columns = list(range(n))
x = rows
y = columns
t = False

for si in s:
    if si[0] == 1:
        _, a, b = si
        x[a - 1], x[b - 1] = x[b - 1], x[a - 1]
    elif si[0] == 2:
        _, a, b = si
        y[a - 1], y[b - 1] = y[b - 1], y[a - 1]
    elif si[0] == 3:
        t = not t
        x, y = y, x
    else:
        _, a, b = si
        if t:
            a, b = b, a
        print(rows[a - 1] * n + columns[b - 1])
