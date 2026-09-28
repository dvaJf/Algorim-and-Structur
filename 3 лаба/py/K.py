n = int(input())
h = list(map(int, input().split()))

P = [0] * (n + 1)
for k in range(n):
    P[k + 1] = P[k] + h[k]

stack = []
res = -1
resl = 1
resr = 1

for i in range(n + 1):
    if i < n:
        a = h[i]
    else:
        a = -1

    while len(stack) > 0 and h[stack[-1]] >= a:
        b = h[stack.pop()]

        if len(stack) > 0:
            l = stack[-1]
        else:
            l = -1

        c = P[i] - P[l + 1]

        if b * c > res:
            res = b * c
            resl = l + 2
            resr = i

    stack.append(i)

print(res)
print(resl, resr)
