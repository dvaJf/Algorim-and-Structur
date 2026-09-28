z = []

a = input().split()
for x in a:
    if x in "0123456789":
        z.append(x)
    else:
        a = z.pop()
        b = z.pop()
        z.append(eval(f"{b}{x}{a}"))
print(z[0])
