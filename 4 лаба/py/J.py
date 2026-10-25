import heapq
n, p = map(int, input().split())
p = []
for i in range(n):
    a, b = map(int, input().split())
    p.append((a, a + b - 1, i + 1))

p.sort()
h = []
lvl = [0] * (n + 1)
c1 = 0
for l, r, i in p:
    if h and h[0][0] < l:
        e, c = heapq.heappop(h)

    else:
        c1 += 1
        c = c1

    lvl[i] = c
    heapq.heappush(h, (r, c))
print(c1)

a = []
for x in range(c1 + 1):
    a.append([])

for i in range(1, n + 1):
    a[lvl[i]].append(i)

res = []
for x in range(1, c1 + 1):
    for i in a[x]:
        res.append(i)

print(" ".join(map(str, res)))