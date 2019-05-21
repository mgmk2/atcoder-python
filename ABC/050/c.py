from collections import defaultdict

MOD = 10 ** 9 + 7
n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
for ai in a:
    d[ai] += 1
ans = 1
if n % 2:
    for k, v in d.items():
        if k > 0 and v == 2:
            ans *= 2
        elif k == 0 and v == 1:
            ans *= 1
        else:
            ans = 0
            break
        ans = ans % MOD
else:
    for v in d.values():
        if v == 2:
            ans *= 2
        else:
            ans = 0
            break
        ans = ans % MOD
print(ans)
