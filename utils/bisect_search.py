def bisect_search(L, x):
    idx = 0
    start = 0
    end = len(L)
    while(True):
        if x <= L[start]:
            y = start
            break
        elif x > L[end - 1]:
            y = end
            break

        center = start + (end - start) // 2
        if x <= L[center]:
            end = center
        else:
            start = center
    return y

def lower_bound(x, f, start, end):
    # bisect search x in [f(start), f(end - 1)]
    # f: function

    end -= 1
    if x <= f(start):
        return start
    if x > f(end):
        return end + 1

    while start + 1 < end:
        center = start + (end - start) // 2
        if x <= f(center):
            end = center
        else:
            start = center
    return end

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
