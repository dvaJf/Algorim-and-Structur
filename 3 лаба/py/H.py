from collections import deque

n = int(input())

q1 = deque()
q2 = deque()
res = []

for x in range(n):
    a = input().split()

    if len(a) > 1 and a[0] == "*":
        q2.appendleft(a[1])
    elif len(a) > 1 and a[0] == "+":
        q2.append(a[1])
    elif len(a) == 1:
        res.append(q1.popleft())

    if len(q1) < len(q2):
        q1.append(q2.popleft())
    elif len(q1) > len(q2) + 1:
        q2.appendleft(q1.pop())

for x in res:
    print(x)
