n = input()
x = int(n)
f = sum(list(map(int, list(n))))
if x % f == 0:
    print('Yes')
else:
    print('No')
