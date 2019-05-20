s = input()
x = [int(s[:2]), int(s[2:])]
y = [False, False]
for i, xi in enumerate(x):
    if 1 <= xi <= 12:
        y[i] = True
if y[0] and y[1]:
    print('AMBIGUOUS')
elif y[0]:
    print('MMYY')
elif y[1]:
    print('YYMM')
else:
    print('NA')
