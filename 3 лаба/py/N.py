from collections import deque

a = deque(map(int, input().split()))
b = deque(map(int, input().split()))

c = 0

while len(a) > 0 and len(b) > 0:
    c += 1
    if c > 10**6:
        print("botva")
        break

    a1 = a.popleft()
    b1 = b.popleft()

    if (a1 == 0 and b1 == 9) or (a1 > b1 and not (a1 == 9 and b1 == 0)):
        a.append(a1)
        a.append(b1)
    else:
        b.append(a1)
        b.append(b1)


if len(a) == 0:
    print("second", c)
if len(b) == 0:
    print("first", c)
