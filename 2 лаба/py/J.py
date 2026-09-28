n, a, b, w, h = map(int, input().split())

l = 0
r = max(w, h)
res = 0

while l <= r:
    mid = (l + r) // 2

    x1 = w // (a + 2 * mid)
    y1 = h // (b + 2 * mid)
    t1 = x1 * y1

    x2 = w // (b + 2 * mid)
    y2 = h // (a + 2 * mid)
    t2 = x2 * y2

    if t1 >= n or t2 >= n:
        res = mid
        l = mid + 1
    else:
        r = mid - 1

print(res)
