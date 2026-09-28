a, b, c = map(int, input().split())
z = []

for x in range(a):
    z.append(int(input()))

z = sorted(z)


def good(mid):
    z1 = [0] * (a + 1)
    for i in range(1, a + 1):
        z1[i] = z1[i-1]
        if i >= c:
            if z[i-1] - z[i-c] <= mid:
                if z1[i-c] + 1 > z1[i]:
                    z1[i] = z1[i-c] + 1
    return z1[a] >= b


l = 0
r = max(z) - min(z)
res = r

while l <= r:
    mid = (l + r) // 2
    if good(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1

print(res)
