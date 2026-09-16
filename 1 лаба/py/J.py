z = []
while True:
    try:
        z.append(input())
    except EOFError:
        break

for i in range(len(z)):
    for j in range(i + 1, len(z)):
        if z[j] + z[i] > z[i] + z[j]:
            temp = z[i]
            z[i] = z[j]
            z[j] = temp

print("".join(z))

