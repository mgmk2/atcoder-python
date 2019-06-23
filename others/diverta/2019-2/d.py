def solve_dp(m, a, b):
    dp = [0] * (m + 1)
    dp[0] = m
    for ai, bi in zip(a, b):
        w = ai
        v = bi - ai
        for j in range(w, m + 1):
            dp[j] = max(dp[j - w] + v, dp[j])
    return max(dp)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = solve_dp(n, a, b)
ans = solve_dp(m, b, a)
print(ans)
