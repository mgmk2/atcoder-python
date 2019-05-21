import sys

sys.setrecursionlimit(10 ** 5 + 1)

def dfs(i, n, a, L):
    # x + y = n - 1
    # x - y = a
    # x = (n - 1 + a) / 2
    # y = (n - 1 - a) / 2
    if i == n:
        return 1
    if a [i] == 0:
        x = [(n - 1 + a[i]) // 2]
    else:
        x = [(n - 1 + a[i]) // 2, (n - 1 - a[i]) // 2]
    t = 0
    MOD = 10 ** 9 + 7
    for xi in x:
        if L[xi] == 0:
            L[xi] = i + 1
            t += dfs(i + 1, n, a, L)
            L[xi] = 0
    return t % MOD

n = int(input())
a = list(map(int, input().split()))
L = [0 for _ in range(n)]
ans = dfs(0, n, a, L)
print(ans)
