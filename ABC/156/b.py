n, k = map(int, input().split())
ans = 1
x = k
while n >= x:
    x *= k
    ans += 1
print(ans)
