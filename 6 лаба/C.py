a = list(map(int, input().split()))
z = [[0]*a[0] for x in range(a[0])]

for x in range(a[1]):
    q = list(map(int, input().split()))
    z[q[1]-1][q[0]-1] = 1
    z[q[0]-1][q[1]-1] = 1
c = 0
for x in range(len(z)):
    c += sum(z[x])
if c == a[0]**2-a[0]:
    print("YES")
else:
    print("NO")
