n, s, d = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
for x, y in A:
    if x < s and y > d:
        print('Yes')
        break
else:
    print('No')