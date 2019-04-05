n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a = sorted(a, key=lambda x: x[0])
k = 0
i = 0
ans = 0
while(True):
    if m - k > a[i][1]:
        ans += a[i][0] * a[i][1]
        k += a[i][1]
        i += 1
    else:
        ans += a[i][0] * (m - k)
        break
print(ans)
