N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
ans = 0
if N % 2 == 0:
    ans = 2 * (sum(A[N // 2 + 1:]) - sum(A[:N // 2 - 1])) + A[N // 2] - A[N // 2 - 1]
else:
    x = 2 * (sum(A[N // 2 + 1:]) - sum(A[:N // 2 - 1])) - A[N // 2] - A[N // 2 - 1]
    y = 2 * (sum(A[N // 2 + 2:]) - sum(A[:N // 2])) + A[N // 2] + A[N // 2 + 1]
    ans = max(x, y)
print(ans)
