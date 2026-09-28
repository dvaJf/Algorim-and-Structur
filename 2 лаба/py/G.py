n, k = map(int, input().split())
a = []
for x in range(n):
    a.append(int(input()))

l = 1
r = 10000000
res = 0

while l <= r:
    mid = (l + r) // 2
    c = 0
    for x in a:
        c += x // mid

    if c >= k:
        res = mid
        l = mid + 1
    else:
        r = mid - 1

print(res)
