h, w = map(int, input().split())
c = []
for i in range(h):
    c.append(input())
for i in range(2 * h):
    print(c[i // 2])
