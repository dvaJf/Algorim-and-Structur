n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a = sorted(a)


def low(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return l


def hig(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > x:
            r = mid
        else:
            l = mid + 1
    return l


ans = []
for x in b:
    ans.append(str(hig(a, x) - low(a, x)))

print(' '.join(ans))
