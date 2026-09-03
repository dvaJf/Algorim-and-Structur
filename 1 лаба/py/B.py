def InsertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i
        while j >= 1 and a[j-1] > key:
            a[j] = a[j-1]
            j -= 1
        a[j] = key
    return a


a = InsertionSort(list(map(int, input().split())))
print(*a)
