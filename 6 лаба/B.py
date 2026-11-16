e = input()
z = []
for x in range(int(e)):
    z.append(list(map(int, input().split())))
z0 = [[z[i][j] for i in range(len(z))] for j in range(len(z[0]))]
z1 = []
z2 = []

for q in range(len(z0)):
    if sum(z0[q]) == 0:
        z2.append(q+1)
    if sum(z[q]) == 0:
        z1.append(q+1)
print(len(z2))
for x in z2:
    print(x)
print(len(z1))
for x in z1:
    print(x)
