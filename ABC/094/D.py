N = int(input())
A = list(map(int, input().split()))
A.sort()
X = A[-1]
X2 = (X + 1) // 2
dd = A[-1]
for i in range(N - 1):
    d = abs(X2 - A[i])
    if d < dd:
        dd = d
        Y = A[i]
print(X, Y)
