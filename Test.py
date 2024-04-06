class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def get_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level



    def print_tree(self):
        spaces = " " * self.get_level() * 2
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def buildTree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.get_child(TreeNode('HP'))
    laptop.get_child(TreeNode('Mac'))

    cellphone = TreeNode("Cell Phone")
    cellphone.get_child(TreeNode('samsung'))
    cellphone.get_child(TreeNode('iphone'))

    tv = TreeNode('TV')
    tv.get_child(TreeNode('LG'))
    tv.get_child(TreeNode('MI'))

    root.get_child(laptop)
    root.get_child(cellphone)
    root.get_child(tv)

    return root

if __name__ == '__main__':
    root = buildTree()
    root.print_tree()

        