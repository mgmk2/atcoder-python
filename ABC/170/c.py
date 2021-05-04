x, n = map(int, input().split())
p = list(map(int, input().split()))
y = None
if x in p:
    for i in range(102):
        if i in p:
            continue
        if y is None or abs(x - i) < y:
            y = abs(x - i)
            ans = i
else:
    ans = x
print(ans)
