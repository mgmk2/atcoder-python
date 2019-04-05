s = list(map(int, input().split('/')))
if s[1] < 4 or (s[1] == 4 and s[2] <= 30):
    print('Heisei')
else:
    print('TBD')
