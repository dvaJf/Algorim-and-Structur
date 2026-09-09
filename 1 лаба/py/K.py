n = int(input())
a = list(range(1, n+1))

for i in range(2, n):
    temp = a[i]
    a[i] = a[i // 2]
    a[i // 2] = temp
    
print(*a)
