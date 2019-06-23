n = int(input())
ans = 0
for i in range(1, int(n ** 0.5) + 1):
    if i * (i + 1) >= n:
        break
    if (n - i) % i == 0:
        ans += (n - i) // i
print(ans)
