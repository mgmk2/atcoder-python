n = int(input())
w = list(map(int, input().split()))
a = [0]
for i in w:
    a.append(a[-1] + i)
ans = a[-1]
for i in range(1, n):
    ans = min(ans, abs(a[-1] - 2 * a[i]))
print(ans)
