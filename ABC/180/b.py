n = int(input())
x = list(map(int, input().split()))
man = sum(map(abs, x))
euc = sum(map(lambda k: k ** 2, x)) ** 0.5
che = max(map(abs, x))
print(man)
print(euc)
print(che)
