n = int(input())
a = list(map(int, input().split()))
c = [0, 0, 0]
MOD = 10 ** 9 + 7
ans = 1
for i, ai in enumerate(a):
    flag = False
    x = 0
    for j, cj in enumerate(c):
        if cj == ai:
            x += 1
            if not flag:
                flag = True
                c[j] += 1
    ans *= x
    ans %= MOD
print(ans)
