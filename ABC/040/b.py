n = int(input())
ans = n
for i in range(1, int(n ** 0.5) + 1):
    ans = min(ans, abs(i - n // i) + n % i)
print(ans)
