n = int(input())
for i in range(1, 10):
    if n % i == 0 and 0 < n // i < 10:
        print('Yes')
        break
else:
    print('No')
