from itertools import combinations


def lower_bound(f, start, end):
    # bisect search x in [f(start), f(end - 1)]
    # f: function

    end -= 1
    if not f(start):
        return start
    if f(end):
        return end + 1

    while start + 1 < end:
        center = start + (end - start) // 2
        if not f(center):
            end = center
        else:
            start = center
    return end


def is_greater_equal(x, p):
    ans = 0
    for pi in p:
        ans <<= 1
        ans |= pi >= x
    return ans


n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]


def func(x):
    s = set()
    for p in m:
        s.add(is_greater_equal(x, p))
    for si in s:
        for sj in s:
            for sk in s:
                if si | sj | sk == 31:
                    return True
    return False


print(lower_bound(func, 1, 10 ** 9 + 1) - 1)
