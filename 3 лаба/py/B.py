a = input()
z = []
flag = "yes"
for x in range(len(a)):
    if a[x] in "([{":
        z.append(a[x])
    else:
        if len(z) <= 0:
            flag = "no"
            break

        if a[x] == ")" and z[-1] == "(":
            z.pop()
        elif a[x] == ")":
            flag = "no"
            break

        if a[x] == "]" and z[-1] == "[":
            z.pop()
        elif a[x] == "]":
            flag = "no"
            break

        if a[x] == "}" and z[-1] == "{":
            z.pop()
        elif a[x] == "}":
            flag = "no"
            break

if len(z) != 0:
    flag = "no"


print(flag)
