n = int(input())
a = list(map(int, input().split()))
for ai in a:
    if ai % 2 == 0 and (ai % 3 > 0 and ai % 5 > 0):
        print('DENIED')
        break
else:
    print('APPROVED')
