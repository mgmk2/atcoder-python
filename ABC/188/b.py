n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for ai, bi in zip(a, b):
    ans += ai * bi
if ans == 0:
    print('Yes')
else:
    print('No')