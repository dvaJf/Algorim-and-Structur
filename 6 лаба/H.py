a = int(input())
z = []
for x in range(int(a)):
    r = list(map(int, input().split()))
    z.append([r, False])
x1, x2 = list(map(int, input().split()))


def dfs(b, c, target, z1):
    global z
    z1.append(b)
    if b == target:
        return z1
    c += 1
    z[b-1][1] = True

    for x in range(a):

        if z[b-1][0][x] == 1 and z[x][1] == False:
                
    

z1 = []

if len(dfs(x1, 0, x2, z1)) == 0:
    print(-1)
else:
    print(len(z1)-1)
    print(*z1)
