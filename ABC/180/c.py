n = int(input())

k = 1
small = []
large = []

while k ** 2 <= n:
    if n % k == 0:
        small.append(k)
        if k != n // k:
            large.append(n // k)
    k += 1
print(*(small + large[::-1]), sep='\n')
