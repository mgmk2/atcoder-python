n = int(input())
v = list(map(int, input().split()))
v.sort(reverse=True)
ans = 0
b = 1
for i in range(n - 1):
    b *= 2
    ans += v[i] / b
ans += v[-1] / b
print(ans)
