sn = input()
k = int(input())
d = len(sn)

dp1 = [[0 for j in range(k + 1)] for i in range(d + 1)] # 未満
dp2 = [[0 for j in range(k + 1)] for i in range(d + 1)] # 未確定
dp2[0][0] = 1
for i in range(d):
    for j in range(k):
        if sn[i] == '0':
            dp2[i + 1][j] += dp2[i][j]
        else:
            dp2[i + 1][j + 1] += dp2[i][j] # i桁目が1以上で同じ場合
            dp1[i + 1][j + 1] += (int(sn[i]) - 1) * dp2[i][j] # i桁目が1以上N[i]未満の場合
            dp1[i + 1][j] += dp2[i][j] # i桁目が0の場合

        dp1[i + 1][j] += dp1[i][j]
        dp1[i + 1][j + 1] += dp1[i][j] * 9
    dp1[i + 1][k] += dp1[i][k]
    dp2[i + 1][k] += dp2[i][k]
print(dp1[-1][-1] + dp2[-1][-1])
