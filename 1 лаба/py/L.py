a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = 0
for x in range(len(a)):
    c += a[x]*b[len(a)-x-1]
print(c)

