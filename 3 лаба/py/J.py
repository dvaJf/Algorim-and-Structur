n = int(input())

for i in range(n):
    r = input().split()
    k = int(r[0])
    a = [float(x) for x in r[1:]]
    tr = sorted(a)
    z = []
    id = 0
    for x in range(len(a)):

        if a[x] == tr[id]:
            id += 1
        else:
            z.append(a[x])

        while len(z) > 0:
            if z[-1] == tr[id]:
                z.pop()
                id += 1
            else:
                break

    print(int(id == len(tr)))
