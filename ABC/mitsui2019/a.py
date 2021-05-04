m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

print(int(m2 == m1 + 1 and d2 == 1))
