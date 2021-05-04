s = input()
t = input()

table = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

for i, si in enumerate(s):
    table_pre = table[i]
    table_cur = table[i + 1]
    for j, tj in enumerate(t):
        if si == tj:
            table_cur[j + 1] = table_pre[j] + 1
        else:
            table_cur[j + 1] = max(table_cur[j], table_pre[j + 1])

ls, lt = len(s), len(t)
ans = ''
while ls and lt:
    if table[ls][lt] == table[ls][lt - 1]:
        lt -= 1
    elif table[ls][lt] == table[ls - 1][lt]:
        ls -= 1
    else:
        ans = s[ls - 1] + ans
        ls -= 1
        lt -= 1
print(ans)
