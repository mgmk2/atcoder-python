x = [int(input()) for i in range(5)]
k = int(input())
for i in range(1, 5):
    for xi in x[:i]:
        if x[i] - xi > k:
            print(':(')
            exit()
print('Yay!')
