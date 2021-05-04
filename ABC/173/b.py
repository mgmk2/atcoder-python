from collections import defaultdict

n = int(input())
d = defaultdict(int)
for i in range(n):
    s = input()
    d[s] += 1

print(f'AC x {d["AC"]}')
print(f'WA x {d["WA"]}')
print(f'TLE x {d["TLE"]}')
print(f'RE x {d["RE"]}')
