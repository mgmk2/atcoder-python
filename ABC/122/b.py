S = input()
l = len(S)
x = 0
for i in range(l):
    j = i + x + 1
    while(j <= l):
        k = i
        flag = True
        while(k < j):
            if S[k] not in ['A', 'C', 'G', 'T']:
                flag = False
                break
            else:
                k += 1
        if flag:
            x = j - i
        j += 1
print(x)
