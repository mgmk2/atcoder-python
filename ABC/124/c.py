s = list(map(int, list(input())))
s0 = s[::2]
s1 = s[1::2]
x0 = sum(s0)
x1 = sum(s1)
print(min(x0 + len(s1) - x1, x1 + len(s0) - x0))
