N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]
M.sort()
print((X - sum(M)) // M[0] + N)
