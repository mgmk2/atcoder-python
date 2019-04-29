a_s = input()
b_s = input()
if a_s == b_s:
    print('EQUAL')
elif len(a_s) > len(b_s):
    print('GREATER')
elif len(a_s) < len(b_s):
    print('LESS')
else:
    a = list(map(int, list(a_s)))
    b = list(map(int, list(b_s)))
    for ai, bi in zip(a, b):
        if ai > bi:
            print('GREATER')
            break
        elif ai < bi:
            print('LESS')
            break
