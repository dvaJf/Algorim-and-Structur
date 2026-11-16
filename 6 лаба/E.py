a, b = input().split()
z = []
for x in range(int(a)):
    z.append([list(map(int, input().split())), False])

def bfs(b, z):
    if b[0][1]==True:
        return z
    z.append(b[0][0])
    b[0][1]=True
    bfs(b,z)
