n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = [ai for ai in a if ai != x]
print(*ans)