o = input()
e = input()
lo = len(o)
le = len(e)
s = ''
for i in range(min(lo, le)):
    s += o[i] + e[i]
if lo > le:
    s += o[-1]
print(s)
