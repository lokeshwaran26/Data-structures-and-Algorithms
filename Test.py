class BinarySearchTree:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addchild(self,data):
        if data == self.data:
            return False
        
        if data < self.data:
            if self.left:
                self.left.addchild(data)

            else:
                self.left = BinarySearchTree(data)

        else:
            if self.right:
                  self.right.addchild(data)

            else:
                self.right = BinarySearchTree(data)

    def search(self,data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search(data)
            
            else:
                return False
            
        if data > self.data:
            if self.right:
                return self.right.search(data)
            
            else:
                return False
            
    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()
        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right.delete(val)

        else:

            if self.left is None and self.right is None:
                return None

            if self.left is None:
                return self.right

            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
        

def buildTree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.addchild(elements[i])

    return root


if __name__ == '__main__':
    nums = [ 7, 1, 4, 5, 6, 8, 2]
    root1 = buildTree(nums)
    print(root1.inOrderTraversal())
    print(root1.search(4))
    root1.delete(6)
    print(root1.inOrderTraversal())
            