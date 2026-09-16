def qick(a):
    if len(a) <= 1:
        return a
    mid = []
    l = []
    r = []
    b = a[int(len(a)//2)]
    for x in a:
        if x < b:
            l.append(x)
        if x == b:
            mid.append(x)
        if x > b:
            r.append(x)

    return qick(l) + mid + qick(r)


a = int(input())
b = list(map(int, input().split()))
print(*qick(b))
