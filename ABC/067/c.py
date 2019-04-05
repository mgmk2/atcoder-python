N = int(input())
a = list(map(int, input().split()))
t = (sum(a))
x = t
ans = 10 ** 10
for ai in a[:-1]:
    x -= 2 * ai
    if ans > abs(x):
        ans = abs(x)
print(ans)
