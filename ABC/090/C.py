n, m = map(int, input().split())
if n > 1 and m > 1:
    ans = (n - 2) * (m - 2)
else:
    ans = abs(max(n, m) - 2)
print(ans)
