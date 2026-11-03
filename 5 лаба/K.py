class Node:
    def __init__(self, k):
        self.k = k
        self.l = None
        self.r = None


class derevo:
    def __init__(self):
        self.root = None
        self.z = []
        self.flag = "YES"

    def add(self, k):
        self.aflag = "DONE"
        self.root = self._add(self.root, k)
        return self.aflag

    def _add(self, node, k):
        if node is None:
            return Node(k)

        if k == node.k:
            self.aflag = "ALREADY"
        elif k < node.k:
            node.l = self._add(node.l, k)
        else:
            node.r = self._add(node.r, k)
        return node

    def search(self, k):
        return self._search(self.root, k)

    def _search(self, node, k):
        if node is None:
            return "NO"
        if k == node.k:
            return "YES"
        elif k < node.k:
            return self._search(node.l, k)
        else:
            return self._search(node.r, k)

    def delete(self, k):
        self.dflag = False
        self.root = self._delete(self.root, k)
        if self.dflag:
            return "DONE"
        else:
            return "CANNOT"

    def _delete(self, node, k):
        if node is None:
            return None

        if k < node.k:
            node.l = self._delete(node.l, k)
        elif k > node.k:
            node.r = self._delete(node.r, k)
        else:
            self.dflag = True

            if node.l is None:
                return node.r
            elif node.r is None:
                return node.l

            mxl = node.l
            while mxl.r is not None:
                mxl = mxl.r

            node.k = mxl.k
            node.l = self._delete(node.l, mxl.k)

        return node

    def mmax(self):
        if self.root.r is None:
            node = self.root.l
            while node.r is not None:
                node = node.r
            return node.k

        node = self.root
        node1 = node.r

        while node1.r is not None:
            node = node1
            node1 = node1.r

        if node1.l is not None:
            node1 = node1.l
            while node1.r is not None:
                node1 = node1.r
            return node1.k

        return node.k

    def obvd(self):
        self._obvd(self.root)

    def _obvd(self, node):
        if node is None:
            return 0

        lh = self._obvd(node.l)
        rh = self._obvd(node.r)

        if abs(lh - rh) > 1:
            self.flag = "NO"

        return max(lh, rh) + 1

    def n(self, k):
        return self._n(self.root, k, -1)

    def _n(self, node, k, node1):
        if node is None:
            return node1

        if node.k >= k:
            return self._n(node.l, k, node.k)
        else:
            return self._n(node.r, k, node1)


tree = derevo()

n = int(input())

flag = False
y = 0

for x in range(n):
    a = input().split()
    a1 = int(a[1])

    if a[0] == '+':
        if flag:
            a1 = (a1 + y) % 10**9
        tree.add(a1)
        flag = False

    elif a[0] == '?':
        y = tree.n(a1)
        print(y)
        flag = True
