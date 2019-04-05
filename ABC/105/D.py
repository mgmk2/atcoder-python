N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0]
b = 0
for i in range(N):
    b += A[i]
    B.append(b % M)
B.sort()
ans = 0
k = 1
C = []
for i in range(N):
    if B[i] == B[i + 1]:
        k += 1
    else:
        C.append(k)
        k = 1
C.append(k)
for k in C:
    if k > 1:
        ans += k * (k - 1) // 2
print(ans)
