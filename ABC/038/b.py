d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))
x = [d1[i] == d2[j] for j in range(2) for i in range(2)]
print('YES' if any(x) else 'NO')
