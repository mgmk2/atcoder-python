def count_p(x, n):
    y = 0
    i = n
    while(True):
        if i == 0:
            return 0
        xx = x - (n - i) + 3 - 2 ** (i + 1)
        if xx >= 0:
            y = 2 ** i - 1
            if xx > 0:
                y += count_p(xx - 1, i) + 1
            break
        else:
            i -= 1
    return y

n, x = map(int, input().split())
ans = count_p(x, n + 1)
print(ans)
