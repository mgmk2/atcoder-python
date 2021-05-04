n, m = map(int, input().split())
x = [None for _ in range(n)]
flag = True
for i in range(m):
    s, c = map(int, input().split())
    if x[s - 1] is None:
        x[s - 1] = c
    elif x[s - 1] != c:
        flag = False

if flag:
    ans = None
    start = 0 if n == 1 else 10 ** (n - 1)
    for k in range(start, 10 ** n):
        for ki, xi in zip(str(k), x):
            if xi is None:
                continue
            elif ki != str(xi):
                break
        else:
            ans = k
            break
    if ans is None:
        print(-1)
    else:
        print(ans)
else:
    print(-1)
