
class stek:
    def __init__(self):
        self.z = []
        self.c = 0

    def push(self, k):
        self.c += 1
        self.z.append(k)
        print("ok")

    def pop(self):
        if self.c == 0:
            print("error")
            return
        self.c -= 1
        print(self.z.pop())

    def back(self):
        if self.c == 0:
            print("error")
            return
        print(self.z[-1])

    def size(self):
        print(self.c)

    def clear(self):
        self.z = []
        self.c = 0
        print("ok")


s = stek()
while True:
    z = input().split()
    a = z[0]
    if a == "push":
        n = int(z[1])
        s.push(n)
    elif a == "pop":
        s.pop()
    elif a == "back":
        s.back()
    elif a == "size":
        s.size()
    elif a == "clear":
        s.clear()
    elif a == "exit":
        print("bye")
        break
