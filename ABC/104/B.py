S = input()
k = 0
if S[0] == 'A' and S[2:-1].count('C') == 1:
    for i in range(len(S)):
        if S[i].isupper():
            if k == 2:
                print('WA')
                exit()
            k += 1
    print('AC')
else:
    print('WA')
