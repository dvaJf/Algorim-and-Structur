import heapq

n, m = map(int, input().split())
start = {1: n}
end = {n: 1}
h = [(-n, 1)]
a = {}
res = []

for i in range(1, m + 1):
    q = int(input())

    if q > 0:
        while h and (h[0][1] not in start or start[h[0][1]] != h[0][1] - h[0][0] - 1):
            heapq.heappop(h)

        if not h or -h[0][0] < q:
            res.append(-1)
            continue

        s = heapq.heappop(h)[1]
        e = start.pop(s)
        end.pop(e)
        a[i] = (s, s + q - 1)
        res.append(s)
        s += q

    else:
        if -q not in a:
            continue

        s, e = a.pop(-q)
        if s - 1 in end:
            s = end.pop(s - 1)
            start.pop(s)

        if e + 1 in start:
            e = start.pop(e + 1)
            end.pop(e)

    if s <= e:
        start[s] = e
        end[e] = s
        heapq.heappush(h, (s - e - 1, s))

for x in res:
    print(x)