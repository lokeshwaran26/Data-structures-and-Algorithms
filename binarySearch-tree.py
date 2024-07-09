class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinarySearchTree(data)

        else:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_orderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.in_orderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_orderTraversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data

        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:

            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.right

            # min_val = self.right.find_min()  --------> Mininum vale in the right sub tree
            # self.data = max_val
            # self.right = self.right.delete(val)

            # max_val = self.left.find_max() --------------> maxinum value in the left sub tree node to reinitatize
            # self.data = max_val
            # self.right = self.right.delete(val)

        return self

    def insert(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.insert(val)
            else:
                self.left = BinarySearchTree(val)

        if val > self.data:
            if self.right:
                self.right = self.right.insert(val)
            else:
                self.right = BinarySearchTree(val)

        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    nums = [17, 4, 1, 20, 9, 23, 18, 34]
    root1 = build_tree(nums)
    print(root1.in_orderTraversal())
    print(root1.search(4))
    root1.delete(20)
    root1.delete(9)
    print(root1.in_orderTraversal())
