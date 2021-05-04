import bisect

def find(l, n, M, X, D):
    r = bisect.bisect_left(X, X[l] + D[l])
    y = 1
    R = r
    for i in range(l, min(r, n - 1)):
        if M[i] == 0:
            M, yi, ri = find(i + 1, n, M, X, D)
            M[i] += yi
            y += yi
            R = max(R, ri)
    return M, y, R

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
A.sort()
X = [a[0] for a in A]
D = [a[1] for a in A]
M = [0 for _ in range(n)]
l = 0
while l < n - 1:
    M, _, l = find(l, n, M, X, D)
print(M)
