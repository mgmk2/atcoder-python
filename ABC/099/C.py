def log(x, y):
    i = 0
    while(y ** i <= x):
        i += 1
    return i - 1

N = int(input())
if N < 6:
    ans = N
else:
    a = log(N, 6)
    b = log(N, 9)
    print(a)
    print(b)
    m = [6**i for i in range(1, a + 1)] + [9**j for j in range(1, b + 1)]
    m.sort(reverse=True)
    nn = N
    i = 0
    ans = 0
    while(True):
        print(nn, m[i], nn // m[i])
        ans += nn // m[i]
        nn = nn % m[i]
        i += 1
        if i == len(m):
            ans += nn
            break
print(ans)
