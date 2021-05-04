def is_cross(la, lb, x1, x2):
    ya1 = la[0] * x1 + la[1]
    ya2 = la[0] * x2 + la[1]
    yb1 = lb[0] * x1 + lb[1]
    yb2 = lb[0] * x2 + lb[1]
    if ya1 == yb1:
        return False
    return (ya1 - yb1) * (ya2 - yb2) <= 0

def get_line(c, x, y):
    return [c, y - c * x]

t = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xa = sum([ti * ai for ti, ai in zip(t, a)])
xb = sum([ti * bi for ti, bi in zip(t, b)])
if xa / sum(t) == xb / sum(t):
    print('infinity')
else:
    ans = 0
    t_pre = 0
    da = 0
    db = 0
    while(True):
        ans_t = 0
        for ti, ai, bi in zip(t, a, b):
            t_post = t_pre + ti
            la = get_line(ai, t_pre, da)
            lb = get_line(bi, t_pre, db)
            ans_t += is_cross(la, lb, t_pre, t_post)
            t_pre = t_post
            da += ti * ai
            db += ti * bi

        if ans_t == 0:
            break
        ans += ans_t
    print(ans)
