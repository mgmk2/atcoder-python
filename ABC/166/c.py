n, m = map(int, input().split())
h = list(map(int, input().split()))
x = [1 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if h[a - 1] >= h[b - 1]:
        x[b - 1] = 0
    if h[a - 1] <= h[b - 1]:
        x[a - 1] = 0
print(sum(x))
