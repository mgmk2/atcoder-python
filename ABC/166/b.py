n, k = map(int, input().split())
a = set()
for i in range(k):
    d = int(input())
    a |= set(map(int, input().split()))
print(n - len(a))
