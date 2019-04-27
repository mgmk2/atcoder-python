n = int(input())
a = list(map(int, input().split()))
a_abs = []
n_minus = 0
for ai in a:
    if ai < 0:
        n_minus += 1
        a_abs.append(-1 * ai)
    else:
        a_abs.append(ai)
if n_minus % 2 == 0:
    print(sum(a_abs))
else:
    a_abs.sort()
    print(sum(a_abs[1:]) - a_abs[0])
