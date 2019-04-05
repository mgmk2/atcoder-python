a = int(input())
b = int(input())
c = int(input())
x = int(input())
ans = 0
for i in range(a + 1):
    for j in range(b + 1):
        xx = x - (500 * i + 100 * j)
        if xx >= 0 and xx % 50 == 0 and xx // 50 <= c:
            ans += 1
print(ans)
