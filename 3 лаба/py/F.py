from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

d = deque()

for x in range(n):
    while d and d[-1] > a[x]:
        d.pop()

    d.append(a[x])

    if x >= k:
        if a[x - k] == d[0]:
            d.popleft()

    if x >= k - 1:
        print(d[0])
