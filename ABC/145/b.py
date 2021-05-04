N = int(input())
s = input()
if N % 2 == 0 and s[:N // 2] == s[N // 2:]:
    print('Yes')
else:
    print('No')
