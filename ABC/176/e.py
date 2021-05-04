from collections import defaultdict

def get_keys_of_max_value(d):
    v_max = 0
    keys = []
    for k, v in d.items():
        if v_max < v:
            v_max = v
            keys = [k]
        elif v_max == v:
            keys.append(k)
    return keys, v_max

h, w, m = map(int, input().split())
targets = {tuple(map(int, input().split())) for _ in range(m)}
n_r = defaultdict(int)
n_c = defaultdict(int)
for x, y in targets:
    n_r[x] += 1
    n_c[y] += 1

rows, n_r_max = get_keys_of_max_value(n_r)
columns, n_c_max = get_keys_of_max_value(n_c)

for r in rows:
    for c in columns:
        if (r, c) not in targets:
            print(n_r_max + n_c_max)
            break
    else:
        continue
    break
else:
    print(n_r_max + n_c_max - 1)
