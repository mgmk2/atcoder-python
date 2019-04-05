x = list(map(int, list(input())))
y = [0] * 4
for i in range(8):
    y[0] = x[0]
    s = y[0]
    p = list(map(int, list(format(i, '03b'))))
    for j in range(3):
        y[j + 1] = (2 * p[j] - 1) * x[j + 1]
        s += y[j + 1]
    if s == 7:
        print('{}{:+d}{:+d}{:+d}=7'.format(y[0], y[1], y[2], y[3]))
        exit()
