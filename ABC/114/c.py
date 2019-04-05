n = int(input())
a = len(str(n))
ans = 0
x = 9
x2 = 4
for i in range(3, a):
    x *= 3
    x2 *= 2
    ans += x - x2 * 3 + 3
b = 0
l = ['3', '5', '7']
while(True):
    c = 3 ** (a - 1)
    s = ''
    bb = b
    for i in range(a):
        s += l[bb // c]
        bb = bb % c
        c = c // 3
    if int(s) > n or s.count('7') == a:
        break
    elif s.count('3') and s.count('5') and s.count('7'):
        ans += 1
    b += 1
print(ans)
