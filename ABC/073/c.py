N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
count = 1
ans = 0
for i in range(N - 1):
    if A[i] == A[i + 1]:
        count += 1
    else:
        ans += count % 2
        count = 1
print(ans + count % 2)
