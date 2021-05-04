def dfs(V, x, n):
    if len(V) == n:
        p = 0
        for xi in x:
            a, b, c, d = xi
            if V[b - 1] - V[a - 1] == c:
                p += d
        return p

    p = 0
    for j in range(V[-1], 10):
        p = max(p, dfs(V + [j], x, n))
    return p

n, m, q = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(q)]
print(dfs([0], x, n))
