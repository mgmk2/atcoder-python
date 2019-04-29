def value_and_count(x):
    d = {}
    for xi in x:
        if xi in d.keys():
            d[xi] += 1
        else:
            d[xi] = 1
    return d

def comb(n, k):
    k = min(n - k, k)
    denominator = 1 # 分母
    numerator = 1 # 分子
    for i in range(k):
        denominator *= i + 1
        numerator *= n - i
    return numerator // denominator

n, a, b = map(int, input().split())
v = list(map(int, input().split()))
d_v = value_and_count(v)
v.sort(reverse=True)
sum_v = sum(v[:a])
mean_v = sum_v / a
print(mean_v)

ans = 0
d_vk = None
for k in range(a, b + 1):
    vk = v[:k]
    sum_vk = sum(vk)
    if sum_vk / k < mean_v:
        break

    if d_vk is None:
        d_vk = value_and_count(vk)
    else:
        d_vk[vk[-1]] += 1

    ans_k = 1
    for vi, ci in d_vk.items():
        ans_k *= comb(d_v[vi], ci)
    ans += ans_k

print(ans)
