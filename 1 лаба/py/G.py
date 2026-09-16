def CountSort(a):
    s = [0] * 101
    for x in a:
        s[x] += 1

    i = 0
    for j in range(101):
        for x in range(s[j]):
            a[i] = j
            i += 1


b = list(map(int, input().split()))
CountSort(b)
print(*b)

