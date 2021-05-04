x = map(int, input().split())
for i, xi in enumerate(x):
    if xi == 0:
        print(i + 1)
        break
