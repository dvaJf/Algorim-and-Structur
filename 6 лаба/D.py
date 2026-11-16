a, b = list(map(int, input().split()))
z = []
for x in range(int(a)):
    r = list(map(int, input().split()))
    z.append([r, False])
c = 0


def dfs(b):
    global c, z
    c += 1
    z[b-1][1] = True

    for x in range(a):

        if z[b-1][0][x] == 1 and z[x][1] == False:

            dfs(x+1)


dfs(b)
print(c)
