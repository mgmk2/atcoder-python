n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
MOD = 10 ** 9 + 7
xx = 0
yy = 0
for i, xi in enumerate(x):
    xx += (2 * i + 1 - n) * xi
for i, yi in enumerate(y):
    yy += (2 * i + 1 - m) * yi
print(xx * yy % MOD)
