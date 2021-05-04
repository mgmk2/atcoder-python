n = input()
a = list(map(int, input().split()))
s = set(a)
if len(s) == len(a):
    print('YES')
else:
    print('NO')
