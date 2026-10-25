import heapq

n, k, p = map(int, input().split())

z = [int(input()) for x in range(p)]

pos = [10**10] * p
last = {}

for i in range(p - 1, -1, -1):
    car = z[i]
    if car in last:
        pos[i] = last[car]
    last[car] = i

pol = set()
nx = {}
h = []
res = 0

for i in range(p):
    car = z[i]

    if car in pol:
        nx[car] = pos[i]
        heapq.heappush(h, (10**10 - pos[i], car))
        continue

    if len(pol) == k:
        while h:
            pos1, car1 = heapq.heappop(h)
            if car1 in pol and nx[car1] == 10**10 - pos1:
                pol.remove(car1)
                break

    pol.add(car)
    res += 1
    nx[car] = pos[i]
    heapq.heappush(h, (10**10 - pos[i], car))

print(res)