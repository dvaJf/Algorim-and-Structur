e = input()
z = []
for x in range(int(e)):
    z.append(list(map(int, input().split())))
f = "YES"
for q in range(len(z)):
    for w in range(len(z)):
        if q == w and z[q][w] == 1:
            f = "NO"
            break
        if z[q][w] != z[w][q]:
            f = "NO"
            break
print(f)
