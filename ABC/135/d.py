MOD = 10 ** 9 + 7
s = input()
n = len(s)
dp = [[0 for j in range(13)] for i in range(n + 1)]
dp[0][0] = 1
dpi = dp[0]
for i, si in enumerate(s):
    dpi1 = dp[i + 1]
    if si == '?':
        k_list = range(10)
    else:
        k_list = [int(si)]
    for j in range(13):
        xij = dpi[j]
        for k in k_list:
            dpi1[(j * 10 + k) % 13] += xij
    for j in range(13):
        dpi1[j] %= MOD
    dpi = dpi1
print(dp[-1][5])
