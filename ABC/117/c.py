N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

if N == 1:
    print(X[-1] - X[0])
else:
    a = []
    for i in range(len(X) - 1):
        a.append(X[i + 1] - X[i])
    a.sort()
    print(X[-1] - X[0] - sum(a[-(N - 1):]))
