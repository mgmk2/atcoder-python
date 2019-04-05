x, y = map(int, input().split())
ans = 1
while(True):
    x *= 2
    if x <= y:
        ans += 1
    else:
        break
print(ans)
