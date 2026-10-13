a = [9, 8, 8, 6, 6, 6, 4, 3, 3, 2, 0]
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def f(q):
    l = -1
    r = len(a)

    while l + 1 < r:
        mid = (l+r)//2

        if q > a[mid]:
            r = mid
        else:
            l = mid

    if l >= len(a)-1:
        print(-1)
    else:
        print(l+1)
    

c = [6, 11, 2, 7, -3, 0]
for x in c:
    f(x)
