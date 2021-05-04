h, w = map(int, input().split())
if min(h, w) == 1:
    ans = 1
else:
    ans = w * (h // 2)
    if h % 2:
        ans += (w + 1) // 2
print(ans)
