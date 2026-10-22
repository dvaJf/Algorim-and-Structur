import heapq

a = []
while True:
    try:
        s = input().split()
        if not s:
            continue
        if s[0] == 'ADD':
            heapq.heappush(a, -int(s[1]))
        elif s[0] == 'CLEAR':
            a = []
        elif s[0] == 'EXTRACT':
            if a:
                print(-heapq.heappop(a))
            else:
                print("CANNOT")
    except EOFError:
        break
