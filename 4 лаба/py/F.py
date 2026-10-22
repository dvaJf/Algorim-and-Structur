import heapq

n = int(input())
z = []
for x in range(n):
    q, w = list(map(int, input().split()))
    z.append((q, w))

z = sorted(z)
z1 = []

for t in z:
    t1 = t[0] + t[1]
    if z1 and t[0] >= z1[0]:
        heapq.heappop(z1)
    heapq.heappush(z1, t1)

print(len(z1))
