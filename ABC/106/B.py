n = int(input())
ans = 0
for i in range(1, n + 1, 2):
    k = 0
    for j in range(1, int(i**0.5 + 1)):
        if i % j == 0:
            k += 1
    if k == 4:
        ans += 1
print(ans)
