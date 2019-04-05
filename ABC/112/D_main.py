N, M = map(int, input().split())
a = int(M**0.5)
ans = []
for i in range(1, a + 1):
    if M % i == 0:
        if N * i <= M:
            ans.append(i)
        if N <= i:
            ans.append(int(M / i))
print(max(ans))
