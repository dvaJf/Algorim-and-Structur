class Point:
    x = 0
    y = 0
    dist = 0


n = int(input())
m = []
for i in range(n):
    a, b = map(int, input().split())
    p = Point()
    p.x = a
    p.y = b
    p.dist = a * a + b * b
    m.append(p)

m.sort(key=lambda p: p.dist)

for p in m:
    print(p.x, p.y)

