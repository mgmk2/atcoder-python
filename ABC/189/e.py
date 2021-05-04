def matmul(x, y):
    d1 = len(x)
    d2 = len(y[0])
    out = [[0 for _ in range(d2)] for _ in range(d1)]
    for i in range(d1):
        for j in range(d2):
            for k in range(len(x[i])):
                out[i][j] += x[i][k] * y[k][j]
    return out

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
s = [input().split() for _ in range(m)]

q = int(input())
query = [[] for _ in range(m + 1)]
for i in range(q):
    a, b = map(int, input().split())
    query[a].append((i, b - 1))

result = [None for _ in range(q)]

for index, b in query[0]:
    result[index] = xy[b]

A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
op1 = [[0, -1, 0],
       [1,  0, 0],
       [0,  0, 1]]

op2 = [[ 0, 1, 0],
       [-1, 0, 0],
       [ 0, 0, 1]]

op3 = [[-1, 0, 0],
       [ 0, 1, 0],
       [ 1, 0, 1]]

op4 = [[1,  0, 0],
       [0, -1, 0],
       [0,  1, 1]]

for i, si in enumerate(s):
    if si[0] == '1':
        A = matmul(A, op1)
    elif si[0] == '2':
        A = matmul(A, op2)
    elif si[0] == '3':
        p = int(si[1])
        op3[2][0] = 2 * p
        A = matmul(A, op3)
    else:
        p = int(si[1])
        op4[2][1] = 2 * p
        A = matmul(A, op4)

    for index, b in query[i + 1]:
        x, y = xy[b]
        r = matmul([[x, y, 1]], A)
        result[index] = r[0][:2]

for r in result:
    print(*r)