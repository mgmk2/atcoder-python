def upper_bound(x, f, start, end):
    # bisect search x in [f(start), f(end - 1)]
    # f: function

    end -= 1
    if x < f(start):
        return start
    if x >= f(end):
        return end + 1

    while start + 1 < end:
        center = start + (end - start) // 2
        if x < f(center):
            end = center
        else:
            start = center
    return end

x = input()
m = int(input())

if len(x) == 1:
    print(int(int(x) <= m))

else:
    y = list(map(int, x))
    y = y[::-1]
    d = max(y)

    def f(n):
        z = 0
        k = 1
        for yi in y:
            z += k * yi
            k *= n
        return z

    ans = upper_bound(m, f, 1, 10 ** 18 + 1) - (d + 1)
    print(max(0, ans))