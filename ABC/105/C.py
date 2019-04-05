N = int(input())
if N == 0:
    print('0')
else:
    k = 1
    ans = []
    while(True):
        if N % ((-2) ** k) == 0:
            ans.append('0')
        else:
            ans.append('1')
            N -= (-2) ** (k - 1)
        if N == 0:
            break
        else:
            k += 1
    print(''.join(ans[::-1]))
