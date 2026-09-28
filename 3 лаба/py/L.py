h = list(map(int, input().split()))
n = h[0]
h = h[1:]
stack = []
res = 0

for i in range(n + 1):
    if i < n:
        a = h[i]
    else:
        a = 0

    while len(stack) > 0 and h[stack[-1]] >= a:
        b = h[stack.pop()]

        if len(stack) > 0:
            l = stack[-1]
        else:
            l = -1

        c = i - l - 1
        res = max(res, b * c)

    stack.append(i)

print(res)
