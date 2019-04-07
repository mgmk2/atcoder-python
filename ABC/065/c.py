x = list(map(int, input().split()))
MOD = 10 ** 9 + 7
if abs(x[0] - x[1]) > 1:
    print(0)
else:
    ans = 1
    for i in range(max(x)):
        for j in range(2):
            ans *= max(1, x[j] - i)
            ans = ans % MOD
    if x[0] == x[1]:
        print(ans * 2 % MOD)
    else:
        print(ans)
