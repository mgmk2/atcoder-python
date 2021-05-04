n, t = map(int, input().split())
a = list(map(int, input().split()))

s = set()
s.add(0)

for ai in a:
    for ti in list(s):
        if ti + ai <= t:
            s.add(ti + ai)

print(max(s))
