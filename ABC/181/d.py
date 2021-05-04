import collections

s = input()
ss = list(map(int, list(s)))
c = collections.Counter(ss)

if len(s) == 1:
    if s == '8':
        print('Yes')
    else:
        print('No')
else:
    if len(s) < 3:
        p = len(s)
    else:
        p = 3
    for x in range(8, 1001, 8):
        d = collections.defaultdict(int)
        for xs in list(('{:0' + str(p) + 'd}').format(x)):
            d[int(xs)] += 1
        for k, v in d.items():
            if c[k] < v:
                break
        else:
            print('Yes')
            break
    else:
        print('No')
