n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
x = [v[i] - c[i] for i in range(n)]
ans = 0
for xi in x:
    if xi > 0:
        ans += xi
print(ans)
