n, k = map(int, input().split())
a = list(map(int, input().split()))
q = list(map(int, input().split()))

for x in q:
    l=0
    r=n-1
    f = "NO"
    while l<=r:
        mid = (l+r)//2
        
        if a[mid] == x:
            f = "YES"
            break
        elif a[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    print(f)