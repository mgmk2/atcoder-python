h = int(input())
n = 0
while h > 0:
    h = h // 2
    n += 1
print(2 ** n - 1)
