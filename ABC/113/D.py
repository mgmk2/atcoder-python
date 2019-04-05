h, w, k = map(int, input().split())
mod = 10 ** 9 + 7
t = [1, 1, 2, 3, 5, 8, 13, 21]
if w == 1:
    print(1)
    exit()
s = [1] + [0 for _ in range(w - 1)]
for i in range(h):
    ss = [None for _ in range(w)]
    ss[0] = (s[0] * t[w - 1] + s[1] * t[w - 2]) % mod
    ss[w - 1] = (s[w - 1] * t[w - 1] + s[w - 2] * t[w - 2]) % mod
    for j in range(1, w - 1):
        ss[j] = (s[j - 1] * t[j - 1] * t[w - j - 1] + s[j] * t[j] * t[w - j - 1] + s[j + 1] * t[w - j - 2] * t[j]) % mod
    s = ss
print(s[k - 1])
