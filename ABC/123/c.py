n = int(input())
limit = [int(input()) for _ in range(5)]
limit.sort()
print(((n + limit[0] - 1) // limit[0]) + 4)
