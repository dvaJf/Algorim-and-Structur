a = list(set(map(int, input().strip().split()[:-1])))
a = sorted(a)
for x in range(len(a)):
    print(a[x])