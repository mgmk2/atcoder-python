n = int(input())

k = 1
ans = 0
while n > k * k:
    if n % k == 0:
        if k % 2 == 1 and n // k % 2 == 1:
            ans += 4
        elif k % 2 == 1 or n // k % 2 == 1:
            ans += 2
    k += 1
if n == k * k and k % 2 == 1:
    ans += 2
print(ans)
