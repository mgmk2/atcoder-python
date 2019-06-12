L = input()
MOD = 10 ** 9 + 7
dp1 = [0] * len(L)
dp2 = [0] * len(L)
dp1[0] = 1
dp2[0] = 2
for i in range(1, len(L)):
    s = L[i]
    if s == '0':
        dp1[i] = (3 * dp1[i - 1]) % MOD
        dp2[i] = dp2[i - 1]
    else:
        dp1[i] = (3 * dp1[i - 1] + dp2[i - 1]) % MOD
        dp2[i] = (2 * dp2[i - 1]) % MOD
print((dp1[-1] + dp2[-1]) % MOD)
