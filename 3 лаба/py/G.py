n = int(input())

r = list(map(int, input().split()))
z = sorted(r)
id = 0
z1 = []
for x in range(len(r)):
    if r[x] == z[id]:
        id += 1
    else:
        while len(z1) > 0 and z1[-1] == z[id]:
            id += 1
            z1.pop()

        z1.append(r[x])

while len(z1) > 0 and z1[-1] == z[id]:
    id += 1
    z1.pop()

if (len(z1) == 0):
    print("YES")
else:
    print("NO")
