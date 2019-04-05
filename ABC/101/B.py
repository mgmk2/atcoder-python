N = input()
S = list(map(int, list(N)))
if int(N) % sum(S) == 0:
    print('Yes')
else:
    print('No')
