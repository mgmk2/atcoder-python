a, b, w = map(int, input().split())
w *= 1000
if w // a == w // b and w % a > 0 and w % b > 0:
    print('UNSATISFIABLE')
else:
    print((w + b - 1) // b, w // a)