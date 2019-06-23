n, k = map(int, input().split())
m = (n - 1) * (n - 2) // 2
if k > m:
    print(-1)
else:
    print(n - 1 + m - k)
    for i in range(2, n + 1):
        print(1, i)
    t = 0
    for i in range(2, n + 1):
        for j in range(i + 1, n + 1):
            if t >= m - k:
                break
            print(i, j)
            t += 1
