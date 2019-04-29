N, T = map(int, input().split())
t = list(map(int, input().split()))
t_pre = 0
ans = T
for i in range(N):
    ans += min(T, t[i] - t_pre)
    t_pre = t[i]
print(ans)
