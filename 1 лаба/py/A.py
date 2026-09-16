def SelectionSort(b):
    temp = 0
    for i in range(len(b)):
        max = -10**9
        for j in range(i, len(b)):
            if b[j] > max:
                max = b[j]
                maxi = j
        temp = b[i]
        b[i] = max
        b[maxi] = temp
    return b


b = SelectionSort(list(map(int, input().split())))
print(*b)

