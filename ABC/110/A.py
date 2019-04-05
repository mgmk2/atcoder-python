x = list(map(int, input().split()))
x = sorted(x, reverse=True)
print(x[0]*10 + x[1] + x[2])
