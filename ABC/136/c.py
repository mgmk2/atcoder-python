n = int(input())
h = list(map(int, input().split()))
h0min = h[0]
h0max = h[0]
for i in range(1, n):
    hi = h[i]
    if hi < h0min:
        print('No')
        break
    h0min = max(h0min, hi - 1)
    h0max = hi
else:
    print('Yes')
