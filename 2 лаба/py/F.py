n, x, y = map(int, input().split())

l = 0
r = (n-1)*min(x, y)
res = 0
while l <= r:
    mid = (l+r)//2
    if (mid//x)+(mid//y) >= n-1:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
if n == 1:
    print(min(x, y))
else:
    print(res + min(x, y))
