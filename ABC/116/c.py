def argmin(x):
    xx = 1000
    ans = 0
    for i, xi in enumerate(x):
        if xi < xx:
            xx = xi
            ans = i
    return ans

def count_water(x, threshold):
    if len(x) == 1:
        return x[0] - threshold
    i = argmin(x)
    y = x[i] - threshold
    if i > 0:
        y += count_water(x[:i], x[i])
    if i < len(x) - 1:
        y += count_water(x[i + 1:], x[i])
    return y

n = int(input())
h = list(map(int, input().split()))
print(count_water(h, 0))
