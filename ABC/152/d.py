n = int(input())

C = [[0 for j in range(10)] for i in range(10)]

for k in range(1, n + 1):
    sk = str(k)
    C[int(sk[0])][int(sk[-1])] += 1

ans = 0
for i in range(1, 10):
    for j in range(i, 10):
        ans += ((i != j) + 1) * C[i][j] * C[j][i]
print(ans)
