n, k, c = map(int, input().split())
s = input()
idx = 0
forward = []
while idx < len(s) and len(forward) < k:
    if s[idx] == 'o':
        forward.append(idx)
        idx += c + 1
    else:
        idx += 1

idx = len(s) - 1
backward = []
while idx >= 0 and len(backward) < k:
    if s[idx] == 'o':
        backward.append(idx)
        idx -= c + 1
    else:
        idx -= 1

for f, b in zip(forward, backward[::-1]):
    if f == b:
        print(f + 1)
