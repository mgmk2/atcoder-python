def prime(x):
    y = list(range(1, x + 1))
    y[0] = 0
    x_sqrt = x ** 0.5
    for i in y:
        if i > x_sqrt:
            break
        elif i == 0:
            continue
        for not_prime in range(2 * i, x + 1, i):
            y[not_prime - 1] = 0
    return [i for i in y if i > 0]
