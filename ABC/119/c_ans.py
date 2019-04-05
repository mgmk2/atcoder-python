n, *x = map(int, input().split())
L = [int(input()) for _ in range(n)]

def dfs(i, a, b, c):
    if i == len(L):
        if min(a, b, c) > 0:
            return abs(x[0] - a) + abs(x[1] - b) + abs(x[2] - c) - 30
        else:
            return 10 ** 9

    ret0 = dfs(i + 1, a, b, c)
    ret1 = dfs(i + 1, a + L[i], b, c) + 10
    ret2 = dfs(i + 1, a, b + L[i], c) + 10
    ret3 = dfs(i + 1, a, b, c + L[i]) + 10
    return min(ret0, ret1, ret2, ret3)

print(dfs(0, 0, 0, 0))
