n = int(input())
red = [list(map(int, input().split()))[::-1] for _ in range(n)]
red.sort()
red = red[::-1]
blue = [list(map(int, input().split())) for _ in range(n)]
blue.sort()
blue = blue[::-1]
ans = 0
for i in range(n):
    bb = blue[i]
    for j in range(n - ans):
        if bb[0] >= red[j][1] and bb[1] >= red[j][0]:
            ans += 1
            del red[j]
            break
print(ans)
