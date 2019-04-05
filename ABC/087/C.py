n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
s = [a[0][0], sum(a[1])]
ans = s[0] + s[1]
for i in range(1, n):
    s[0] += a[0][i]
    s[1] -= a[1][i - 1]
    ans = max(ans, s[0] + s[1])
print(ans)
