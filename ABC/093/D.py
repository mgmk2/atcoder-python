def search(a, b):
    if a == b or a + 1 == b:
        return 2 * a - 2
    else:
        c = int((a * b - 1) ** 0.5)
        if c * (c + 1) >= a * b:
            return 2 * c - 2
        else:
            return 2 * c - 1

Q = int(input())
for i in range(Q):
    x = list(map(int, input().split()))
    x.sort()
    print(search(x[0], x[1]))
