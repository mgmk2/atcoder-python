import bisect

q = int(input())
a = []
b = 0
for i in range(q):
    s = list(input().split())
    if s[0] == '1':
        ai = int(s[1])
        bi = int(s[2])
        bisect.insort_left(a, ai)
        b += bi
    else:
        if len(a) % 2:
            idx = len(a) // 2
            print(str(a[idx]), str(b))
        else:
            idx = len(a) // 2 - 1
            print(str(a[idx]), str(b + (a[idx + 1] - a[idx])))
