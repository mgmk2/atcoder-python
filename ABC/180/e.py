def get_dist(city_a, city_b):
    return abs(city_a[0] - city_b[0]) + abs(city_a[1] - city_b[1]) + max(0, city_b[2] - city_a[2])

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]

dp = [[None for j in range(n)] for i in range(1 << n)]
dp[1][0] = 0
for S in range(1, (1 << n), 2):
    for next in range(1, n):
        if S & (1 << next):
            continue
        dp[S | (1 << next)][next] = min([dp[S][cur] + get_dist(city[cur], city[next]) for cur in range(n) if S & (1 << cur) and dp[S][cur] is not None])
print(min([dp[-1][i] + get_dist(city[i], city[0]) for i in range(n) if dp[-1][i] is not None]))
