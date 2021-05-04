n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = a[0] + 2 * sum(a[1:n // 2])
if n % 2:
    ans += a[n // 2]
print(ans)
