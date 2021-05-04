n, k = map(int, input().split())
h = list(map(int, input().split()))
ans = sum(map(lambda x: x >= k, h))
print(ans)
