N, Q = map(int, input().split())
S = input()
Ls = len(S)
x = [0 for _ in range(Ls)]
for i in range(Ls - 1):
    x[i + 1] = x[i]
    if S[i:i + 2] == 'AC':
        x[i + 1] += 1
for i in range(Q):
    l, r = map(int, input().split())
    print(x[r - 1] - x[l - 1])
