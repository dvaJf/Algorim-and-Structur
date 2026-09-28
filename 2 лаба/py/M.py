a, b = map(int, input().split())
z = []

for x in range(a):
    z.append(int(input()))

l = 0
r = 10**10
res = 0

while l <= r:
    mid = (r+l)//2
    c = 0
    if mid == 0:
        res = 0
        break
    for x in z:
        c += x // mid
    if c >= b:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)
