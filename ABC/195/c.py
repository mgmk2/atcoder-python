n = int(input())
k = 1
ans = 0
x = 999
while x <= n:
    ans += n - x
    k += 1
    x = 10 ** (3 * k) - 1
print(ans)