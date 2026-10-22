
class Hip():
    def __init__(self):
        self.z = []

    def l(self):
        a = len(self.z)
        return a

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
        a = self.z.pop()
        self.vniz()
        return a


n = int(input())
z = Hip()
q = list(map(int, input().split()))
for x in q:
    z.Insert(x)
z1 = []
while z.l() > 0:
    z1.append(z.Extract())
for x in z1[::-1]:
    print(x)
