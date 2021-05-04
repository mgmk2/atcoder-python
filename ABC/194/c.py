n = int(input())
a = list(map(int, input().split()))
b = [0]
for ai in a:
    b.append(b[-1] + ai)
x1 = sum([(i + 1) * ai ** 2 for i, ai in enumerate(a[1:])])
x2 = sum([(n - i - 1) * ai ** 2 for i, ai in enumerate(a[:-1])])
x3 = -2 * sum([b[i] * ai for i, ai in enumerate(a)])
print(x1 + x2 + x3)