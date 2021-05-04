import bisect

n, c_prime = map(int, input().split())
schedule = set()
x = [list(map(int, input().split())) for _ in range(n)]
for a, b, c in x:
    schedule.add(a)
    schedule.add(b + 1)

schedule = sorted(list(schedule))
costs = [0 for _ in range(len(schedule) + 1)]

for a, b, c in x:
    start = bisect.bisect_left(schedule, a)
    costs[start] += c
    end = bisect.bisect_left(schedule, b + 1)
    costs[end] -= c

ans = 0
p = 0
t = 0
for s, cost in zip(schedule, costs):
    ans += (s - t) * min(c_prime, p)
    p += cost
    t = s
print(ans)