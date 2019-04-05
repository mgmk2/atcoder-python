a, b, k = map(int, input().split())
j = 0
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        j += 1
        if j == k:
            break
print(i)
