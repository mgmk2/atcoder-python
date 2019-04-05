N = int(input())
S = input()
ans = 0
for i in range(1, N):
    m = len(set(S[:i]) & set(S[i:]))
    if m > ans:
        ans = m
print(ans)
