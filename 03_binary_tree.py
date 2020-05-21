class Node():
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

    def preorder(self):
        print(self.item, end=" ")
        if self.lchild is not None:
            self.lchild.preorder()
        if self.rchild is not None:
            self.rchild.preorder()

    def inorder(self):
        if self == None:
            return
        if self.lchild is not None:
            self.lchild.inorder()
        print(self.item, end=" ")
        if self.rchild is not None:
            self.rchild.inorder()

    def postorder(self):
        if self == None:
            return
        if self.lchild is not None:
            self.lchild.postorder()
        if self.rchild is not None:
            self.rchild.postorder()
        print(self.item, end=" ")


class Tree():
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        while True:
            cur = queue.pop(0)
            if cur.lchild == None:
                cur.lchild = node
                return
            queue.append(cur.lchild)
            if cur.rchild == None:
                cur.rchild = node
                return
            queue.append(cur.rchild)

    def breadth_travel(self):
        if self.root == None:
            print('empty tree')
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur != None:
                print(cur.item)
                queue.append(cur.lchild)
                queue.append(cur.rchild)

    def preorder(self):
        if self.root is None:
            return
        self.root.preorder()

    def inorder(self):
        if self.root is None:
            return
        self.root.inorder()

    def postorder(self):
        if self.root is None:
            return
        self.root.postorder()


if __name__ == "__main__":
    tree = Tree()
    for i in range(10):
        tree.add(i)
    print(f'preorder: ', end=" ")
    tree.preorder()
    print(' ')
    print(f'inorder: ', end=" ")
    tree.inorder()
    print(' ')
    print(f'postorder: ', end=" ")
    tree.postorder()
    print(' ')
