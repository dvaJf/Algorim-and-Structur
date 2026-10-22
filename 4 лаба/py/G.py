import heapq

n = int(input())
z = []
h = []

for i in range(n):
    a = int(input())
    z.append(a)
    heapq.heappush(h, (max(1000 - a, 1), i))

t = 0
pos = 0

while True:
    t1, akvar = heapq.heappop(h)
    run_t = t + abs(pos - akvar)

    if run_t > t1:
        print(t1)
        break

    t = t1
    pos = akvar

    z[akvar] += 1
    t2 = t1 + max(1000 - z[akvar], 1)
    heapq.heappush(h, (t2, akvar))
