from collections import defaultdict

MOD = 998244353
n, s = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

X = [([0], s)]
y = defaultdict(int)
for ai in a:
    Xi = []
    for l, r in X:
        if r < ai:
            continue
        Xi.append((l, r))
        if r == ai:
            y[len(l)] += 1
            continue
        elif r - ai >= ai:
            Xi.append((l + [ai], r - ai))
    X = Xi

ans = 0
for k, v in y.items():
    ans += v * pow(2, n - k, MOD) % MOD
    ans %= MOD
print(ans)
