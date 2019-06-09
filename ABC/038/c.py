def combnk(n, k):
    x = n
    y = 1
    for i in range(1, k):
        x *= n - i
        y *= i + 1
    return x // y

n = int(input())
a = list(map(int, input().split()))

# 単調増加になる区間を探索
lr = []
l = 0
for i in range(1, n):
    if a[i - 1] >= a[i]:
        lr.append([l, i - 1])
        l = i
lr.append([l, n - 1])

# 単調増加する区間毎に組み合わせを算出して足し合わせる
ans = 0
for l, r in lr:
    ans += r - l + 1 + combnk(r - l + 1, 2)
print(ans)
