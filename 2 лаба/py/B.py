n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

for x in range(k):
    v = q[x]

    if v <= a[0]:
        print(a[0])
        continue
    if v >= a[-1]:
        print(a[-1])
        continue
    l = 0
    r = n - 1
    while r - l > 1:
        mid = (l + r) // 2
        if a[mid] < v:
            l = mid
        else:
            r = mid

    if v - a[l] <= a[r] - v:
        print(a[l])
    else:
        print(a[r])
