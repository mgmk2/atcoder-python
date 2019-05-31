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
