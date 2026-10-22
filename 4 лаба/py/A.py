
class Hip():
    def __init__(self):
        self.z = []

    def verh(self):
        i = len(self.z) - 1
        while i > 0 and self.z[i] > self.z[(i - 1) // 2]:
            self.z[i], self.z[(i - 1) // 2] = self.z[(i - 1) // 2], self.z[i]
            i = (i - 1) // 2

    def vniz(self):
        i = 0
        while 2*i+1 < len(self.z):
            if 2*i+2 == len(self.z):
                if self.z[i] < self.z[2*i+1]:
                    self.z[i], self.z[2*i+1] = self.z[2*i+1], self.z[i]
                break
            if self.z[i] < self.z[2*i+2] and self.z[i] < self.z[2*i+1]:
                if self.z[2*i+2] > self.z[2*i+1]:
                    self.z[i], self.z[2*i+2] = self.z[2*i+2], self.z[i]
                    i = 2*i+2
                else:
                    self.z[i], self.z[2*i+1] = self.z[2*i+1], self.z[i]
                    i = 2*i+1
            elif self.z[i] < self.z[2*i+2]:
                self.z[i], self.z[2*i+2] = self.z[2*i+2], self.z[i]
                i = 2*i+2
            elif self.z[i] < self.z[2*i+1]:
                self.z[i], self.z[2*i+1] = self.z[2*i+1], self.z[i]
                i = 2*i+1
            else:
                break

    def Insert(self, k):
        self.z.append(k)
        self.verh()

    def Extract(self):
        self.z[0], self.z[-1] = self.z[-1], self.z[0]
        print(self.z.pop())
        self.vniz()


n = int(input())
z = Hip()
for x in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        z.Insert(a[-1])
    else:
        z.Extract()
