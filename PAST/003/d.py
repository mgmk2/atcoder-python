from collections import defaultdict

d = {}
d['####.##.##.####'] = '0'
d['.#.##..#..#.###'] = '1'
d['###..#####..###'] = '2'
d['###..####..####'] = '3'
d['#.##.####..#..#'] = '4'
d['####..###..####'] = '5'
d['####..####.####'] = '6'
d['###..#..#..#..#'] = '7'
d['####.#####.####'] = '8'
d['####.####..####'] = '9'

n = int(input())
x = ['' for _ in range(n)]
for i in range(5):
    s = input()
    for j in range(n):
        x[j] += s[4 * j + 1:4 * (j + 1)]
ans = ''
for j in range(n):
    ans += d[x[j]]
print(ans)
