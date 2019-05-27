s = input()
g = 0
p = 0
ans = 0
for si in s:
    if p + 1 <= g: # パーを出せる
        p += 1
        if si == 'g': # 相手がグーの時は勝ち
            ans += 1
    else: # パーを出せない
        g += 1
        if si == 'p': # 相手がパーの時は負け
            ans -= 1
print(ans)
