def solve(a, b):
    d = {}
    for x in a:
        if x not in d:
            d[x] = 0
        d[x] += 1

    for x in b:
        if x not in d:
            return "NO"
        if d[x] == 0:
            return "NO"
        d[x] -= 1

    for x in d:
        if d[x] != 0:
            return "NO"
    return "YES"


a = input()
b = input()
print(solve(a, b))
