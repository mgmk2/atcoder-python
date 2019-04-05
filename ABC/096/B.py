x = list(map(int, input().split()))
K = int(input())
x.sort()
print(x[0] + x[1] + 2 ** K * x[2])
