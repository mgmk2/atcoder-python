n = int(input())
d = list(map(int, input().split()))
d2 = list(map(lambda x: x * x, d))
print((sum(d) ** 2 - sum(d2)) // 2)
