n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
x.sort(key=lambda x: x[1])
t = 0
for a, b in x:
    t += a
    if t > b:
        print('No')
        break
else:
    print('Yes')
