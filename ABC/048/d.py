s = input()
if (s[0] == s[-1]) ^ (len(s) % 2 == 1):
    print('First')
else:
    print('Second')
