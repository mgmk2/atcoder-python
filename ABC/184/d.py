a, b, c = map(int, input().split())
dp = [[[0 for k in range(101)] for j in range(101)] for i in range(101)]
dp[a][b][c] = 1

n = a + b + c
ans = 0
for ai in range(a, 101):
    for bi in range(b, 101):
        if ai == 100 and bi == 100:
            continue
        for ci in range(c, 101):
            if (ai == 100 and ci == 100) or (bi == 100 and ci == 100):
                continue
            ni = ai + bi + ci
            if 100 in [ai, bi, ci]:
                ans += (ni - n) * dp[ai][bi][ci]
            else:
                p = dp[ai][bi][ci]
                dp[ai + 1][bi][ci] += p * ai / ni
                dp[ai][bi + 1][ci] += p * bi / ni
                dp[ai][bi][ci + 1] += p * ci / ni
print(ans)
