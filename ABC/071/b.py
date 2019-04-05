s = list(set(input()))
d = 'abcdefghijklmnopqrstuvwxyz'
for di in d:
    if di not in s:
        print(di)
        exit()
print('None')
