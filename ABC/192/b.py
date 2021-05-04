S = input()
if S[::2].islower() and (len(S) == 1 or S[1::2].isupper()):
    print('Yes')
else:
    print('No')