N = int(input())
S = input()
ans = N
x = 0
y = S.count('E')
for i in range(N):
    if S[i-1] == 'W' and i > 0:
        x += 1
    if S[i] == 'E':
        y -= 1
    if x + y < ans:
        ans = x + y
print(ans)
