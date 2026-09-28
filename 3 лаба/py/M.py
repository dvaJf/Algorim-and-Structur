n, c = map(int, input().split())
h = []
for i in range(n - 1):
    h.append(int(input()))
res = [0.0] * n

left = [-1] * (n - 1)
right = [-1] * (n - 1)
stack = []
for i in range(n - 1):
    last = -1
    while len(stack) > 0 and h[stack[-1]] < h[i]:
        last = stack.pop()
    left[i] = last
    if len(stack) > 0:
        right[stack[-1]] = i
    stack.append(i)

node = -1
if len(stack) > 0:
    node = stack[0]

l = 0
r = n - 1

while node != -1:
    m = node
    hm = h[m]
    all = r - l + 1
    mx = m - l + 1

    if c >= all * hm:
        break
    elif c <= mx * hm:
        r = m
        node = left[m]
    else:
        for i in range(l, m + 1):
            res[i] = hm
        c -= mx * hm
        l = m + 1
        node = right[m]

for i in range(l, r + 1):
    res[i] = c / (r - l + 1)

for x in res:
    print(round(x, 6))
