a, b = input().split()
ans = 0
a = int(a)
b = list(b.replace('.', ''))
ans += a * int(b[0]) * 100
ans += a * int(b[1]) * 10
ans += a * int(b[2])
print(ans // 100)
