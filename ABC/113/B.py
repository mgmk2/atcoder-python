n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
ans = 1
for i in range(n):
    x = h[i]
    tt = t - x * 0.006
    dtt = abs(tt - a)
    if i == 0:
        dt = dtt
    elif dtt < dt:
        dt = dtt
        ans = i + 1
print(ans)
