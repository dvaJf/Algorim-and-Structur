a, b = map(int, input().split())
t = []
z = []
y = []

for x in range(b):
    ti, zi, yi = map(int, input().split())
    t.append(ti)
    z.append(zi)
    y.append(yi)


def sobrat(i, mid):
    b1 = z[i] * t[i] + y[i]
    f = mid // b1
    g = mid % b1
    e = min(z[i], g // t[i])
    return f * z[i] + e


def good(mid):
    s = 0
    for i in range(b):
        s += sobrat(i, mid)
        if s >= a:
            return True
    return s >= a


l = 0
r = 10**10

res = r

while l <= r:
    mid = (l + r) // 2

    if good(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1

g = []

for i in range(b):
    c = sobrat(i, res)

    if c >= a:
        g.append(a)
        a = 0
    else:
        g.append(c)
        a -= c

print(res)
print(*g)
