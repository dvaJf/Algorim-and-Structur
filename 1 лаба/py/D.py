def BubbleSort(b):
    temp = 0
    с = 0
    for i in range(len(b)):
        for j in range(len(b) - 1 - i):
            if b[j] > b[j + 1]:
                temp = b[j]
                b[j] = b[j + 1]
                b[j + 1] = temp
                с += 1
    return с


a = input()
b = BubbleSort(list(map(int, input().split())))
print(b)
