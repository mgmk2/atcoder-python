n = int(input())
C = [tuple(map(int, input().split())) for _ in range(n)]
C.sort(key=lambda x: 2 * x[0] + x[1], reverse=True)

aoki = sum(map(lambda x: x[0], C))
takahashi = 0
for i, (a, b) in enumerate(C):
    aoki -= a
    takahashi += a + b
    if takahashi > aoki:
        print(i + 1)
        break