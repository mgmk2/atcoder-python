x = int(input())
for i in range(1, 10 ** 5):
    i5 = i ** 5
    flag = False
    for j in range(i):
        j5 = j ** 5
        if i5 + j5 == x:
            flag = True
            print(i, -j)
            break
        elif i5 - j5 == x:
            flag = True
            print(i, j)
    if flag:
        break
