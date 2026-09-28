w, h, n = map(int, input().split())

l = 1
r = n * max(w, h)
res = r

while l <= r:
    mid = (l + r) // 2
    if (mid // w) * (mid // h) >= n:
        res = mid
        r = mid - 1
    else:
        l = mid + 1

print(res)
