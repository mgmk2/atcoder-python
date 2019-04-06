ans = 0
x = [int(input()) for _ in range(5)]
y = 200
for i, xi in enumerate(x):
    xx = xi % 10
    if xx == 0:
        xx = 10
    if y > xx:
        y = xx
        j = i

for i in range(5):
    if i == j:
        ans += x[i]
    else:
        ans += (x[i] + 10 - 1) // 10 * 10
print(ans)
