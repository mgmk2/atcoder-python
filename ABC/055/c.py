n, m = map(int, input().split())
if n >= m // 2:
    ans = m // 2
else:
    ans = n + (m - n * 2) // 4
print(ans)
