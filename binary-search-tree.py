class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
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

    def search(self,val):
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
            elements+= self.right.in_orderTraversal()
        
        return elements


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    countries = ["India ", "Pakistan", "Germany", "USA", "China", "India","UK","USA"]
    country_tree = build_tree(countries)
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))



