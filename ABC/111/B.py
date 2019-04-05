a_str = input()
a = int(a_str)
x, y, z = map(int, list(a_str))
if x*111==a:
    print(a)
elif x*111 > a:
    print(x*111)
else:
    print((x+1)*111)
