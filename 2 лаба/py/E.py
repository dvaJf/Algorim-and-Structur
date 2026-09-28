n, k = map(int, input().split())
a = list(map(int, input().split()))


def cor(mid, a, k):
    z = a[0]
    k = k-1
    for x in range(len(a)):
        if a[x]-z >= mid:
            k -= 1
            z = a[x]
    if k <= 0:
        return True
    return False


l = 0
r = a[-1]-a[0]
res = 0
while l <= r:
    mid = (l+r)//2
    if cor(mid, a, k):
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)
