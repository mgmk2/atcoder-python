s = input()
s_odd = s[::2]
s_even = s[1::2]
if 'L' in s_odd or 'R' in s_even:
    print('No')
else:
    print('Yes')
