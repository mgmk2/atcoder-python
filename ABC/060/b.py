a, b, c = map(int, input().split())
for bi in range(1, b + 1):
    if a * bi % b == c:
        print('YES')
        exit()
print('NO')
