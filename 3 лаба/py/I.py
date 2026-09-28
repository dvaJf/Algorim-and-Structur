data = list(map(int, input().split()))
n = data[0]
a = data[1:] + [123]
z = []
c = 0

for x in a:
    if len(z) > 0 and z[-1] != x:
        с1 = 0
        while с1 < len(z) and z[-1 - с1] == z[-1]:
            с1 += 1

        if с1 >= 3:
            c += с1
            for i in range(с1):
                z.pop()

    if x != 123:
        z.append(x)

print(c)
