a, r, n = map(int, input().split())
# a * r ** (n - 1) <= 10 ** 9
# r ** (n - 1) <= 10 ** 9 // a <= 10 ** 9 / a
if n == 1 or r == 1:
    print(a)
else:
    k = 1
    for i in range(n - 1):
        k *= r
        if a * k > 10 ** 9:
            print('large')
            break
    else:
        print(a * k)
