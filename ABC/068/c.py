N, M = map(int, input().split())
E1 = [1] + [0 for _ in range(N - 1)]
EN = [0 for _ in range(N - 1)] + [1]
for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        E1[b - 1] = 1
    elif b == N:
        EN[a - 1] = 1
for i in range(N):
    if E1[i] * EN[i] == 1:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
