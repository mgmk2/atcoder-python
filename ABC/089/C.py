from itertools import combinations
N = int(input())
s = [input()[0] for _ in range(N)]
s.sort()
x = [s.count('M'), s.count('A'), s.count('R'), s.count('C'), s.count('H')]
ans = 0
for v in combinations(x, 3):
    ans += v[0] * v[1] * v[2]
print(ans)
