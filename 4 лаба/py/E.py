import heapq

n = int(input())
a = list(map(int, input().split()))
heapq.heapify(a)
s1 = 0
while len(a) > 1:
    s = heapq.heappop(a) + heapq.heappop(a)
    s1 += s*0.05
    heapq.heappush(a, s)
print(round(s1, 2))
