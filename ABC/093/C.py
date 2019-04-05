x = list(map(int, input().split()))
x.sort()
n = (x[2] - x[1]) // 2
x[0] += 2 * n
x[1] += 2 * n
ans = 2 * n
n = (x[2] - x[0]) // 2
x[0] += 2 * n
ans += n
x.sort()
if x[1] == x[2]:
    if x[0] == x[1]:
        print(ans)
    else:
        print(ans + 2)
else:
    print(ans + 1)
