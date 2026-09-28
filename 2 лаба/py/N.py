a, k, b, m, x = map(int, input().split())


l = 0
r = 10**20
res = 0
while l <= r:
    mid = (r+l)//2
    if (mid - mid // k) * a + (mid - mid // m) * b >= x:
        res = mid
        r = mid - 1

    else:
        l = mid + 1

print(res)
