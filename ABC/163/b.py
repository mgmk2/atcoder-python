n, m = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
if n >= s:
    print(n - s)
else:
    print(-1)
