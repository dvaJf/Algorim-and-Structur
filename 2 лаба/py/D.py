a, b, c, d = map(int, input().split())

if a < 0:
    a = -a
    b = -b
    c = -c
    d = -d
    
def f(x):
    return a * x**3 + b * x**2 + c * x + d
    
l = -10000000000
r = 10000000000

for x in range(100):
    mid = (l + r) / 2
    if f(mid) > 0:
        r = mid
    else:
        l = mid
        
print(f"{l:.6f}")
