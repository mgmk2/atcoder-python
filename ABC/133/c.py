l, r = map(int, input().split())
if r - l >= 2019:
    print(0)
elif l % 2019 > r % 2019:
    print(0)
else:
    ans = 2019
    for i in range(l % 2019, r % 2019):
        for j in range(i + 1, r % 2019 + 1):
            ans = min(ans, i * j % 2019)
    print(ans)
