n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0
for i in range(n):
    b = abs(k - x[i])
    if x[i] > b:
        ans += 2 * b
    else:
        ans += 2 * x[i]
print(ans)
