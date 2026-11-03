

class Node:
    def __init__(self, k):
        self.k = k
        self.l = None
        self.r = None


class derevo:
    def __init__(self):
        self.root = None

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

    def obvd(self):
        self._obvd(self.root, 0)

    def _obvd(self, node, level):
        if node is None:
            return
        self._obvd(node.l, level + 1)
        if (not (node.l == None) and (node.r == None)) or ((node.l == None) and not (node.r == None)):
            print(str(node.k))
        self._obvd(node.r, level + 1)


tree = derevo()


a = input().split()[:-1]
for x in a:
    tree.add(int(x))
tree.obvd()
