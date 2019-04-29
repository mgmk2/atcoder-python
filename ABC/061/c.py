n, k = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
x = sorted(x, key=lambda x: x[0])
idx = 0
ans = 0
for i in range(n):
    idx += x[i][1]
    if idx >= k:
        ans = x[i][0]
        break
print(ans)
