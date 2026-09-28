c = float(input())

l = 0.0
r = c

for i in range(100):
    mid = (l + r) / 2
    if mid * mid + mid ** 0.5 < c:
        l = mid
    else:
        r = mid

print(f"{l:.6f}")
