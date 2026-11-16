a = int(input())
z = []
for x in range(a):
    r = list(map(int, input().split()))
    z.append([r, 0])
c = 0
flag = 0


def bfs(b):
    global c, z, flag
    if flag == 1:
        return
    c += 1
    z[b][1] = 1

    for x in range(len(z[b][0])):
        if z[b][0][x] == 1 and z[x][1] == 1:
            flag = 1
            return
        elif z[b][0][x] == 1 and z[x][1] == 0:
            bfs(x)

    z[b][1] = 2


for i in range(a):
    if z[i][1] == 0:
        bfs(i)
print(flag)
