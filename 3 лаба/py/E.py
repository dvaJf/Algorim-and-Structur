
class ohered:
    def __init__(self):
        self.z = []
        self.c = 0

    def push_back(self, k):
        self.c += 1
        self.z.append(k)
        print("ok")

    def push_front(self, k):
        self.c += 1
        self.z = [k] + self.z
        print("ok")

    def pop_back(self):
        if self.c == 0:
            print("error")
            return
        self.c -= 1
        print(self.z.pop())

    def pop_front(self):
        if self.c == 0:
            print("error")
            return
        self.c -= 1
        print(self.z.pop(0))

    def front(self):
        if self.c == 0:
            print("error")
            return
        print(self.z[0])

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


s = ohered()
while True:
    z = input().split()
    if not z:
        continue
    a = z[0]
    if a == "push_front":
        n = int(z[1])
        s.push_front(n)
    elif a == "push_back":
        n = int(z[1])
        s.push_back(n)
    elif a == "pop_front":
        s.pop_front()
    elif a == "pop_back":
        s.pop_back()
    elif a == "front":
        s.front()
    elif a == "back":
        s.back()
    elif a == "size":
        s.size()
    elif a == "clear":
        s.clear()
    elif a == "exit":
        print("bye")
        break
