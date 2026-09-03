def splitt(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    l = splitt(arr[:mid])
    r = splitt(arr[mid:])

    return merge(l, r)


def merge(l, r):
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    res.extend(l[i:])
    res.extend(r[j:])
    return res


n = int(input())
a = list(map(int, input().split()))
print(*splitt(a))
