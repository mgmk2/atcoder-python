n, x = map(int, input().split())
s = input()

ans = x
for si in s:
    if si == 'o':
        ans += 1
    else:
        ans = max(0, ans - 1)
print(ans)
