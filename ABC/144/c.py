n = int(input())
ans = 10 ** 13
for i in range(1, int(n ** 0.5 + 1)):
    if n % i == 0:
        j = n // i
        ans = min(ans, i + j - 2)
print(ans)
