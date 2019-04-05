sp = list(input())
t = list(input())
n = len(sp)
for i in range(len(t), n + 1):
    flag = True
    for j in range(len(t)):
        if sp[n - i + j] != t[j] and sp[n - i + j] != '?':
            flag = False
            break
    if flag:
        s = ''
        sp[n - i:n - i + len(t)] = t
        for j in range(n):
            if sp[j] == '?':
                s += 'a'
            else:
                s += sp[j]
        print(s)
        exit()
print('UNRESTORABLE')
