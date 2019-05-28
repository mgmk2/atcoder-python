n, k = map(int, input().split())
s = input()
x = [0]
for i in range(n - 1):
    if s[i:i + 2] in ['01', '10']:
        x.append(i + 1)
y = []
for i in range(len(x)):
    idx = i + 2 * k
    if s[x[i]] == '0':
        if i > 0:
            continue
    else:
        idx += 1

    if idx < len(x):
        y.append(x[idx] - x[i])
    else:
        y.append(n - x[i])
        break
print(max(y))
