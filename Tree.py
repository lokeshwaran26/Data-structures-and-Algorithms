class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level


    def print_data(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_data()


def build_product():
    root = TreeNode('Electonics')


    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode('MAC'))
    laptop.add_child(TreeNode('HP'))
    laptop.add_child(TreeNode('Lenavo'))

    cellphone = TreeNode('Cell Phone')
    cellphone.add_child(TreeNode('iphone'))
    cellphone.add_child(TreeNode('Samsung'))
    cellphone.add_child(TreeNode('Vivo'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('samsung'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    
    return root

if __name__ == '__main__':
    root = build_product()
    root.print_data()
    pass