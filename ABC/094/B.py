N, M, X = map(int, input().split())
A = list(map(int, input().split()))
S = 0
for i in range(M):
    if A[i] < X:
        S += 1
    else:
        print(min(S, M - i))
        exit()
