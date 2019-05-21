n = int(input())
s = input()
x = 0
ans = 0
for si in s:
    if si == 'I':
        x += 1
    elif si == 'D':
        x -= 1
    ans = max(ans, x)
print(ans)
