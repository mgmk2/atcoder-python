import math
N = int(input())
if N < 6:
    ans = N
else:
    a = int(math.log(N, 6))
    b = int(math.log(N, 9))
    print(a)
    print(b)
    m = [6**i for i in range(1, a + 1)] + [9**j for j in range(1, b + 1)]
    m.sort(reverse=True)
    nn = N
    i = 0
    ans = 0
    while(True):
        if nn >= m[i]:
            print(nn, m[i])
            ans += nn // m[i]
            nn = nn % m[i]
        i += 1
        if i == len(m):
            ans += nn
            break
print(ans)
