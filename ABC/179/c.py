n = int(input())
ans = 0
for a in range(1, n):
    ans += max(0, (n - 1) // a)
print(ans)
