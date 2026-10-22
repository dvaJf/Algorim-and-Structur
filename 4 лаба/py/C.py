import sys


class Hip():
    def __init__(self):
        self.z = []

    def l(self):
        return len(self.z)

    def verh(self):
        z = self.z
        i = len(z) - 1
        k = z[i]
        while i > 0:
            p = (i - 1) // 2
            if z[p] > k:
                z[i] = z[p]
                i = p
            else:
                break
        z[i] = k

    def vniz(self):
        z = self.z
        n = len(z)
        i = 0
        if n <= 1:
            return
        k = z[i]
        while True:
            l = 2 * i + 1
            if l >= n:
                break
            s = l
            r = l + 1
            if r < n and z[r] < z[l]:
                s = r
            if z[s] < k:
                z[i] = z[s]
                i = s
            else:
                break
        z[i] = k

    def Insert(self, k):
        self.z.append(k)
        self.verh()

    def Extract(self):
        if len(self.z) == 1:
            return self.z.pop()
        a = self.z[0]
        self.z[0] = self.z.pop()
        self.vniz()
        return a


a = Hip()

for line in sys.stdin:
    s = line.split()
    if not s:
        continue
    if s[0] == 'ADD':
        a.Insert(int(s[-1]))
    elif s[0] == 'CLEAR':
        a.z.clear()
    elif s[0] == 'EXTRACT':
        if a.l() == 0:
            print("CANNOT")
        else:
            print(a.Extract())
