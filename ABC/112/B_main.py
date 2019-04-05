N, T = map(int, input().split())
c = [10000 for _ in range(N)]
for i in range(N):
    c_tmp, t = map(int, input().split())
    if t <= T:
        c[i] = c_tmp
if min(c) > 1000:
    print('TLE')
else:
    print(min(c))
