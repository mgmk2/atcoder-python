def find_ds(h, w):
    ans = h * w
    if h >= 3:
        if h % 3 == 0:
            return 0
        else:
            ans = w
    for i in range(1, w):
        x0 = h * i
        x1 = h // 2 * (w - i)
        x2 = h * w - x0 - x1
        ds = max(x0, x1, x2) - min(x0, x1, x2)
        ans = min(ans, ds)
    return ans

h, w = map(int, input().split())
print(min(find_ds(h, w), find_ds(w, h)))
