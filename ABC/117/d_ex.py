n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(k + 1):
    f = 0
    for j in range(n):
        f += a[j] ^ i
    if ans < f:
        ans = f
        print(i)
print(ans)
