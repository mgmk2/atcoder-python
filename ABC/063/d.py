n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort(reverse=True)
l = len(h)
k = 0
d = a - b
while(True):
    if l == 1:
        print(k + (h[0] + a - 1) // a)
        break
    else:
        kk = max(1, (h[0] - h[1] + d - 1) // d)
        h[0] -= a * kk
        for i in range(1, l):
            h[i] -= b * kk
        h.sort(reverse=True)
        for i in range(l):
            if h[l - i - 1] <= 0:
                del h[l - i - 1]
        l = len(h)
        k += kk
        if l == 0:
            print(k)
            break
