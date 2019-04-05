h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
m = h * w
X = []

for i, ai in enumerate(a):
    X += [i + 1 for _ in range(ai)]

for hi in range(h):
    if hi % 2 == 0:
        print(*X[hi * w:(hi + 1) * w])
    else:
        print(*X[hi * w:(hi + 1) * w][::-1])
