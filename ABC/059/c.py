n = int(input())
a = list(map(int, input().split()))

y = [0, 0]
for k in range(2):
    s = 0
    x = (-1) ** k
    for ai in a:
        si = s + ai
        if si * x > 0:
            s = si
            x *= -1
        else:
            y[k] += abs(si) + 1
            s = x
            x *= -1
print(min(y))
