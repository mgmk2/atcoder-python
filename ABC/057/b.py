n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(n)]
c = [list(map(int, input().split())) for _ in range(m)]
for si in s:
    di = 10 ** 10
    ans = 0
    for j, cj in enumerate(c):
        dij = abs(si[0] - cj[0]) + abs(si[1] - cj[1])
        if dij < di:
            di = dij
            ans = j + 1
    print(ans)
